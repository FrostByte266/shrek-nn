FROM python:3.7

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall -y numpy && pip install numpy==1.16.4

COPY . .
