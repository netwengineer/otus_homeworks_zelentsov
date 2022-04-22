# Build container - sudo docker build . -t python-test                                                                                                                               ─╯
# Start Container - sudo docker run -p 8000:8000 -d python-test
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /
RUN poetry install

COPY *.py /

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]