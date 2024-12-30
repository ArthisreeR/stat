FROM python:3.8-slim
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/
EXPOSE 8008
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8008"]
