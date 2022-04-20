FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR homework3

RUN pip install poetry
RUN poetry config vitrualenvs.create false

COPY poetry.lock pyproject.toml /
RUN poetry install

