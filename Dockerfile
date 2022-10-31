FROM python:3.10.2-buster

LABEL maintainer="songponlekpetch"

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["python", "main.py"]