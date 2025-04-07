# Flight Tracker Middleware API

This project is a middleware API built with **FastAPI** that interacts with the [FlightStats](https://www.flightstats.com/v2/flight-tracker/search) website to scrape flight data, store it in a database using SQLAlchemy, and expose the results via a REST API endpoint.

---

## ✅ Features
- Accepts airline code, flight number, and departure date via GET request
- Scrapes the FlightStats site for relevant flight data
- Stores scraped data in a SQLite database
- Returns stored or newly scraped data in a clean JSON response
- Includes basic test cases using Pytest

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/itsminegitrepo13/Flight-Tracker-Middleware-API
cd flight-tracker-api
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
uvicorn main:app --reload
```

The API will be accessible at: `http://localhost:8000/flight`

---

## 🧱 Project Structure
```
flight-tracker-api/
├── main.py              # FastAPI app and core logic
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic request/response models
├── scraper.py           # BeautifulSoup scraping logic
├── database.py          # DB session and engine setup
├── test_main.py         # Test cases using Pytest
├── requirements.txt     # Project dependencies
└── README.md
```

---

## 🔎 Web Scraping Logic

**URL Targeted**: `https://www.flightstats.com/v2/flight-tracker/search`

- We use `requests` to hit the URL
- `BeautifulSoup` is used to parse and extract:
  - Flight status
  - Departure/arrival airports
  - Departure/arrival times

You may need to adjust the DOM selectors depending on the site’s structure, which could be dynamic. In such cases, integrating tools like **Selenium** may help.

---

## 🔌 API Design

### `GET /flight`
Query Parameters:
- `airline_code`: (e.g. `AA`)
- `flight_number`: (e.g. `100`)
- `departure_date`: (ISO format e.g. `2025-04-01T00:00:00`)

**Response:**
```json
{
  "airline_code": "AA",
  "flight_number": "100",
  "departure_date": "2025-04-01T00:00:00",
  "status": "On Time",
  "departure_airport": "JFK",
  "arrival_airport": "LAX",
  "departure_time": "10:00 AM",
  "arrival_time": "01:00 PM"
}
```

---

## 🧪 Testing

### Install Pytest
```bash
pip install pytest
```

### Run Tests
```bash
pytest test_main.py
```

### Example Test Case (`test_main.py`)
```python
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)

def test_get_flight():
    response = client.get("/flight", params={
        "airline_code": "AA",
        "flight_number": "100",
        "departure_date": "2025-04-01T00:00:00"
    })
    assert response.status_code == 200
    assert "airline_code" in response.json()
```