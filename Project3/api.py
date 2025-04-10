from flask import Flask, request
import numpy as np
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('./models/altlenet5.keras')


@app.route('/summary', methods=['GET'])
def model_info():
    return {
            "version": "v1",
            "name": "hurricane",
            "description": "Classify images of damaged and undamged property",
            "number_of_parameters": 13328
            }

@app.route('/inference', methods=['POST'])
def inference():
    im = request.files.get('image')
    if not im:
        return jsonify({"error": "The `image` field is required"}), 400
    try:
        # Read the image directly as bytes
        image = tf.image.decode_image(im.read(), channels=3)  # Decode as RGB image
        image = tf.image.resize(image, (128, 128)) 
        image = image / 255.0  # Normalize the image
        image = tf.expand_dims(image, axis=0)  # Add batch dimension
        prediction = model.predict(image)
        class_idx = np.argmax(prediction, axis=1)[0]
        label = "damage" if class_idx == 0 else "no_damage"
        return {"prediction": label}
    except Exception as e:
        return {"error": f"Could not process the `image` field; details: {e}"}, 400
# start the development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
