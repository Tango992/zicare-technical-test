from fastapi import FastAPI, Header
from typing import Annotated
import controller
import db
import uvicorn
import helper
import model

app = FastAPI()

@app.get("/doctors")
async def get_all_doctors():
    result = db.get_all_doctors()
    return result

@app.post("/patient/register", response_model=model.RegisterPatientResponse, status_code=201)
async def register_patient(register_patient: model.RegisterPatient):
    id = controller.register_patient(register_patient)
    response = model.RegisterPatientResponse(**register_patient.model_dump(), id=id, )
    return response

@app.post("/patient/login", response_model=model.LoginPatientResponse)
async def login_patient(request_data: model.LoginPatientRequest):
    response = controller.login_patient(request_data)
    return response

@app.post("/patient/appointment")
async def create_appointment(request_data: model.DTOAppointmentRequest, authorization: Annotated[str | None, Header()] = None):
    user_id = helper.verify_token(authorization)
    response = controller.create_appointment(request_data, user_id)
    return response



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)