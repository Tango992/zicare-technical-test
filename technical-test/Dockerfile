FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN  pip install --no-cache-dir --upgrade pip \
  && pip install wheel \
  && pip install coincurve \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]