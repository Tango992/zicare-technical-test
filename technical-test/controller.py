from fastapi import HTTPException
from typing import List
import model
import db
import helper
import re

def register_patient(patient: model.RegisterPatient):
    patient.password = helper.get_password_hash(patient.password)
    id = db.register_patient(patient)
    return id


def login_patient(request_data: model.LoginPatientRequest):
    patient_password = db.get_patient_password_by_phone(request_data.phone)
    valid = helper.verify_password(request_data.password, patient_password)

    if not valid:
        raise HTTPException(status_code=401, detail={"error": "Invalid credentials"})
    
    patient_id = db.get_patient_id_by_phone(request_data.phone)
    token = helper.create_access_token(data={"id": patient_id})

    response = model.LoginPatientResponse(message="Token for 'authorization' header", token=token)
    return response


def create_appointment(request_data: model.DTOAppointmentRequest, user_id: int):
    if not bool(re.search(r"^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", request_data.appointment_date)):
        raise HTTPException(status_code=400, detail={"error": "Invalid date format (YYYY-MM-DD)"})
    
    if not bool(re.search(r"^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$", request_data.appointment_time)):
        raise HTTPException(status_code=400, detail={"error": "Invalid date format (HH:MM:SS)"})
    
    appointment = model.AppointmentRequest(
        patient_id=user_id, 
        doctor_id=request_data.doctor_id, 
        appointment_date=request_data.appointment_date, 
        appointment_time=request_data.appointment_time
    )
    
    id = db.create_appointment(appointment)
    
    response = model.Appointment(
        queue_id=id,
        patient_id=user_id, 
        doctor_id=request_data.doctor_id, 
        appointment_date=request_data.appointment_date, 
        appointment_time=request_data.appointment_time
    )
    return response


def get_all_user_appointments(user_id: int) -> List[model.Appointment]:
    response = db.find_user_appointments(user_id)
    return response

def delete_user_appointment(queue_id: int, user_id: int):
    row_count = db.delete_user_appointment(queue_id, user_id)

    if row_count == 0:
        raise HTTPException(status_code=422, detail={"error": "queue_id and patient_id does not match / not found"})
    return