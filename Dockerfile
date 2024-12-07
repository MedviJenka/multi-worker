ARG version=3.12-slim
FROM python:$version
LABEL author="jenia p"
WORKDIR /app
COPY requirements.txt /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
