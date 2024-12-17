FROM python:3.8-slim
WORKDIR /app
RUN pip install --upgrade pip
COPY stat/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/
EXPOSE 8007
CMD ["tail", "-f", "/dev/null"]
