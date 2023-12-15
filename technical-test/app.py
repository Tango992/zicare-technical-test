from fastapi import FastAPI
from datetime import datetime
import db
import uvicorn
import model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/patient/register", response_model=model.RegisterPatientResponse, status_code=201)
async def register_patient(register_patient: model.RegisterPatient):
    id = db.register_patient(register_patient)
    
    response = model.RegisterPatientResponse(
        **register_patient.model_dump(exclude="password"), 
        id=id, 
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)