FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "app.ini"]