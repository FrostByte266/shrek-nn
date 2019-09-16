FROM tensorflow/tensorflow:latest-gpu-py3

ARG DEBIAN_FRONTEND=noninteractive

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN pip install --ignore-installed --upgrade tensorflow-gpu
RUN apt-get update && apt-get install -y python3-tk

COPY . .
