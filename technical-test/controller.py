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

    response = model.LoginPatientResponse
    response.message = "Bearer token"
    response.token = token
    
    return response
