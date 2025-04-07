from pydantic import BaseModel
from datetime import datetime

class FlightResponse(BaseModel):
    airline_code: str
    flight_number: str
    departure_date: datetime
    status: str
    departure_airport: str
    arrival_airport: str
    departure_time: str
    arrival_time: str

    class Config:
        orm_mode = True
