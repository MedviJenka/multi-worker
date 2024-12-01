# Flask Async Multi-Worker App

This project is a Flask-based application designed to run multiple asynchronous servers using `asyncio` and `Hypercorn`. It includes endpoints to fetch DNS information and resolve IP addresses, making it suitable for scalable and high-performance applications.

---

## Features

### Asynchronous Flask Routes
- Fully async support for non-blocking execution.

### Endpoints
- `/`: Home route for the server.
- `/api/dns`: Fetch the domain name from a given URL.
- `/api/ip`: Resolve the IP address of a given domain.

### Multi-Worker Support
- Run multiple servers concurrently using `asyncio.gather`.

---

## Installation
- navigate to project directory, and install the requirements

```pip install -r requirements.txt```

### Prerequisites
- **Python**: 3.8+
- **Flask**: 2.0+
- **Hypercorn**
- **Httpx**
- **dotenv**


# How to run?

- edit .env file, with desired ports and workers
- run app.py
- access cmd or web and try the examples below

# How to run with docker?

- docker build -t flask-async-app .  
- docker run -d --env-file .env -p 8080:8080 flask-async-app

##### Example 1

```curl -X GET "http://127.0.0.1:81/api/dns?q=https://www.example.com"```


##### Example 1

```curl -X GET "http://127.0.0.1:81/api/ip?q=https://www.example.com"```
