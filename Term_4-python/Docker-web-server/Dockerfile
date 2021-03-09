FROM python:3.8
RUN apt update
RUN apt-get install -y python3-pip
RUN mkdir /opt/source
COPY . /opt/source
WORKDIR /opt/source

CMD ["python3", "main.py"]