# ML-Inference
CS532 Project 2

Collaborators : Kshiti Dinesh Mehta, Shubhankar Ajit Kothari

To build the Docker Image please run the following command:

(The image will be created from the Dockerfile mentioned)

```
docker build -t <Docker Image Name>:<Version> .
```

To create a Docker Container, run the following:

```
docker run -p 5000:5000 <Docker Image Name>:<Version>
```
The command above will create a Docker Container at localhost port 5000.

To send an image to the flask application in the container, use the following command (preferably from a different CLI window):

```
curl -F "file=@<image path name/image name.jpg>" http://127.0.0.1:5000/upload
```
As an example you could try:

```
curl -F "file=@images/fishy.jpg" http://127.0.0.1:5000/upload
```

To download and use image directly (This image has been made using Linux Containers)  :

Download Link : https://drive.google.com/file/d/1XrGhPwX044Ir8v2IpIu33eRFO-0uWm5i/view?usp=sharing
```
docker load < test_image.img
```
```
docker run -p 5000:5000 test:0
```
To ping the server,' and 'curl' commands from above can be used.

To stop the running container and delete all the images from your system, use the following command:

```
docker container ls
```

This command will list down all the containers with their ids, names, etc

To stop the running the container just copy the ID from above and run:

```
docker stop <container id>
```

Now to delete all docker images and containers:

```
docker system prune -f
```

This command will reclaim all the space used up by the non running containers and images.
