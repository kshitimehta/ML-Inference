# ML-Inference
CS532 Project 2

To build the Docker Image please run the following command:

(The image will be created from the Dockerfile mentioned)

```
docker build -t <Docker Image Name>:<Version>
```

To create a Docker Container, run the following:

```
docker run -p 5000:5000 <Docker Image Name>:<Version>
```
The command above will create a Docker Container at localhost port 5000.

To send an image to the flask application in the container, use the following command:

```
curl -F "file=@<file name.jpg>" http://127.0.0.1:5000/upload
```
