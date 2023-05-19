FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn cicd_django_webinar.wsgi --bind 0.0.0.0:8000