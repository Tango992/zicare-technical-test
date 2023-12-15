from pydantic import BaseModel

class RegisterPatient(BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str | None = None
    phone: str
    password: str
    birth_date: str

class RegisterPatientResponse(BaseModel):
    id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str | None = None
    phone: str
    birth_date: str

class LoginPatientRequest(BaseModel):
    phone: str
    password: str

class LoginPatientResponse(BaseModel):
    message: str
    token: str

class Patient(BaseModel):
    id: int | None = None
    first_name: str
    middle_name: str | None = None
    last_name: str | None = None
    phone: str
    password: str
    birth_date: str
    created_at: str | None = None