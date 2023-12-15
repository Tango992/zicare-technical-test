from pydantic import BaseModel

class DTOAppointmentRequest(BaseModel):
    doctor_id: int
    appointment_date: str
    appointment_time: str

class AppointmentRequest(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: str
    appointment_time: str

class Appointment(BaseModel):
    queue_id: int
    patient_id: int
    doctor_id: int
    appointment_date: str
    appointment_time: str

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

class Doctor(BaseModel):
    id: int
    speciality: str
    full_name: str