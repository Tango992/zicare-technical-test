from pydantic import BaseModel, PastDate
from datetime import datetime

class RegisterPatient(BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str | None = None
    phone: str
    password: str
    birth_date: str

class Patient(BaseModel):
    id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str | None = None
    phone: str
    password: str
    birth_date: str
    created_at: str | None = None