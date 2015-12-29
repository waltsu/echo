FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-setuptools
RUN easy_install pip

ADD requirements.txt /src/requirements.txt

WORKDIR /src/
RUN pip install -r requirements.txt

ADD . /src

EXPOSE 5000

CMD ["python", "application.py"]
