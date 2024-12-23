FROM python:3.8-slim
WORKDIR /app
RUN pip install --upgrade pip
COPY statimage/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/
EXPOSE 8008
CMD ["uvicorn", "statimage/statapi_modified.py", "--host", "0.0.0.0", "--port", "8008"]
