from fastapi import HTTPException
import model
import db
import helper

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