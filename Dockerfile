FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/scr/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD bash -c "python manage.py collectstatic --noinput && gunicorn config.wsgi -b 0.0.0.0:8003 -w 3"
