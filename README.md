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
- navigate to project directory
- **run > pip install -r requirements.txt**
### Prerequisites
- **Python**: 3.8+
- **Flask**: 2.0+
- **Hypercorn**
- **Httpx**
- **dotenv**

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
#   m u l t i - w o r k e r  
 