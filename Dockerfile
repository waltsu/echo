FROM waltsu/base

ADD requirements.txt /src/requirements.txt

WORKDIR /src/
RUN pip install -r requirements.txt

ADD . /src

EXPOSE 5000

CMD ["python", "application.py"]
