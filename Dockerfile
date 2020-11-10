FROM python:3.7

COPY ./requirements.txt /ML-Inference/requirements.txt

COPY ./imagenet_class_index.json /ML-Inference/imagenet_class_index.json

COPY ./API.py /ML-Inference/API.py

COPY ./fishy.jpg /ML-Inference/fishy.jpg

WORKDIR /ML-Inference

RUN pip install -r requirements.txt

CMD python API.py