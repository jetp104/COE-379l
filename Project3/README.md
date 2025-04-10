# To use the prebuilt Docker image 

1. Clone the git repo using the following command <pre> git clone https://github.com/jetp104/COE-379l.git</pre> 
2. Run the command <pre> docker pull jetp104/api:1 </pre> This will get the image from DockerHub that was used for the project
3. Get into the folder with the docker file using this command <pre> cd ~/COE-379l/Project3 </pre>
4. Use the command <pre> docker build -t jetp104/api:1 . </pre> to build the image you pulled (Again make sure its in the same location as the Dockerfile) 
5. Then run <pre>  docker run -it --rm -p 5000:5000 jetp104/api </pre> and boom your docker image should be up and running.

# To use the docker-compose.yaml file
1. Make sure you have the entire repo cloned with every location being as its found on this git repo.
2. Run the command <pre> docker-compose up </pre> and boom once again the flask API should be up and running (Note make sure you are in the same directory as the docker-compose.yml file and the api.py file)

# Example Requests 
There are 2 routes for this API a POST and GET route 

For the GET route --> /summary: 
  run the command <pre> curl http://127.0.0.1:5000/summary </pre>  or  <pre> curl localhost:5000/summary </pre> and you'll get the output below: 
  ![image](https://github.com/user-attachments/assets/71ee003e-133c-4467-8073-3d1ea5f6872f)

For the POST route you need to send in a binary message, since I don't have a random one to send in here is an example output from the test script we were given
![image](https://github.com/user-attachments/assets/c2c3806f-1ffe-43d4-915a-afffed9439f7)
