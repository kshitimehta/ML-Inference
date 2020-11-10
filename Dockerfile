FROM python:3.7

WORKDIR /ML-Inference

COPY . /ML-Inference

RUN pip install -r /ML-Inference/requirements.txt

CMD python API.py