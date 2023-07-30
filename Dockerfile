FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/scr/app
COPY requirements.txt ./
RUN pip install -r requirements.txt