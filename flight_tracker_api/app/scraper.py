from datetime import datetime

def scrape_flight_data(airline_code: str, flight_number: str, departure_date: datetime):
    # Mocked scraping data (for demo purpose)
    return {
        "airline_code": airline_code,
        "flight_number": flight_number,
        "departure_date": departure_date,
        "status": "On Time",
        "departure_airport": "JFK",
        "arrival_airport": "LAX",
        "departure_time": "10:00 AM",
        "arrival_time": "1:00 PM"
    }
