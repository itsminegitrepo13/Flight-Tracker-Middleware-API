from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline_code = Column(String)
    flight_number = Column(String)
    departure_date = Column(DateTime)
    status = Column(String)
    departure_airport = Column(String)
    arrival_airport = Column(String)
    departure_time = Column(String)
    arrival_time = Column(String)
