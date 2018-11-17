FROM python:3.7.1

ENV PYTHONUNBUFFERED 1

COPY . /app/
WORKDIR /app/

RUN pip install pipenv
RUN apt-get update
RUN pipenv install --system --deploy --ignore-pipfile


CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]