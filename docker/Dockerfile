FROM python:3.9-slim

WORKDIR /app

COPY ./app /app

COPY ./models.joblib /app/models.joblib

COPY ./docker/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
 && pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]