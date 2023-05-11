FROM python:3.9-slim-buster

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install

COPY . /app

ENV APP_MODULE=main:app

EXPOSE 80

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app"]