FROM python:3.8

WORKDIR /opt/app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
