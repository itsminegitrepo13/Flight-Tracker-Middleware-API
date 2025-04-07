from fastapi import FastAPI, HTTPException, Query
from app import schemas, models, database, scraper
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/flight", response_model=schemas.FlightResponse)
def get_flight(
    airline_code: str = Query(...),
    flight_number: str = Query(...),
    departure_date: datetime = Query(...),
):
    db: Session = database.SessionLocal()
    existing = db.query(models.Flight).filter_by(
        airline_code=airline_code,
        flight_number=flight_number,
        departure_date=departure_date
    ).first()

    if existing:
        return existing

    flight_data = scraper.scrape_flight_data(airline_code, flight_number, departure_date)

    if not flight_data:
        raise HTTPException(status_code=404, detail="Flight not found")

    new_flight = models.Flight(**flight_data)
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight
