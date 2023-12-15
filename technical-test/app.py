from fastapi import FastAPI, Header
from typing import Annotated, List
import controller
import db
import uvicorn
import helper
import model

app = FastAPI()

@app.get("/doctors", response_model=List[model.Doctor])
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


@app.post("/patient/appointment", response_model=model.Appointment, status_code=201)
async def create_appointment(request_data: model.DTOAppointmentRequest, authorization: Annotated[str | None, Header()]):
    user_id = helper.verify_token(authorization)
    response = controller.create_appointment(request_data, user_id)
    return response


@app.get("/patient/appointment", response_model=List[model.Appointment])
async def get_all_appointments(authorization: Annotated[str | None, Header()]):
    user_id = helper.verify_token(authorization)
    response = controller.get_all_user_appointments(user_id)
    return response


@app.delete("/patient/appointment/{queue_id}", response_model=model.Response)
async def delete_appointment(queue_id, authorization: Annotated[str | None, Header()]):
    user_id = helper.verify_token(authorization)
    controller.delete_user_appointment(queue_id, user_id)
    return model.Response(message="Appointment was deleted successfully")


@app.put("/patient/appointment/{queue_id}", response_model=model.Response)
async def delete_appointment(queue_id, request_data: model.DTOAppointmentRequest, authorization: Annotated[str | None, Header()]):
    user_id = helper.verify_token(authorization)
    controller.update_user_appointment(queue_id, user_id, request_data)
    return model.Response(message="Appointment was updated successfully")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)