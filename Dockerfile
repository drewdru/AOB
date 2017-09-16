FROM ubuntu:16.04
USER root

RUN apt update && \
    apt -y install wget libcurl4-openssl-dev build-essential libpq-dev\
    libsqlite3-dev python python-pip python-dev python-numpy-dev binutils\
    python3 python3-pip libssl-dev libffi-dev libgl1-mesa-glx mesa-utils\
    freeglut3-dev libgtk2.0-dev libsm6 libxrender1 gcc g++
RUN apt -y install python3-tk python3-pyqt5 python3-dev\
    python-software-properties
RUN mkdir /code
WORKDIR /code
ADD . /code/
ADD requirements.txt /code/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install charlcd \
    && pip3 install iot_message
