FROM docker.io/python:3.12.7-slim-bookworm AS python

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
