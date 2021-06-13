FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
COPY . /code/

#1 Pull base image
#2 set environment variables
#4 set working directory as `code`
#5 Copy `files` into code directory
#6 Install dependencies