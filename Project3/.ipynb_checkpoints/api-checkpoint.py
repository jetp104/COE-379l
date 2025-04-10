import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from flask import Flask, request
import numpy as np

app = Flask(__name__)


@app.route('/models/altlenet5', methods=['GET'])
def model_info():
    return {
            "version": "v1",
            "name": "hurricane",
            "description": "Classify images of damaged and undamged property",
            "number_of_parameters": 133280
    }

def preprocess_input(im):
    """
    Converts user-provided input into an array that can be used with the model.
    This function could raise an exception.
    """
    # Convert image to numpy array
    d = np.array(im)
    d = d/255
    # Add an extra dimension to simulate batch dimension
    d = np.expand_dims(d, axis=0)
    return d

@app.route('/models/altlenet5', methods=['POST'])
def classify_alt_lenet5():
   model = tf.keras.models.load_model('models/hurricane.keras')
   im = request.json.get('image')
   if not im:
      return {"error": "The `image` field is required"}, 404
   try:
      data = preprocess_input(im)
   except Exception as e:
      return {"error": f"Could not process the `image` field; details: {e}"}, 404
   return { "prediciton": model.predict(data).tolist()}

# start the development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')