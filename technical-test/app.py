from fastapi import FastAPI
import controller
import db
import uvicorn
import model

app = FastAPI()

@app.get("/")
async def root():
    db.get_all_doctors()
    return {"message": "Hello World"}

@app.post("/patient/register", response_model=model.RegisterPatientResponse, status_code=201)
async def register_patient(register_patient: model.RegisterPatient):
    id = controller.register_patient(register_patient)
    response = model.RegisterPatientResponse(**register_patient.model_dump(), id=id, )
    return response

@app.post("/patient/login", response_model=model.LoginPatientResponse)
async def login_patient(request_data: model.LoginPatientRequest):
    response = controller.login_patient(request_data)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)