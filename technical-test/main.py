from fastapi import FastAPI
from datetime import datetime
import uvicorn
import model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/patient/register", response_model=model.Patient, status_code=201)
async def register_patient(register_patient: model.RegisterPatient):
    now = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    patient = model.Patient(**register_patient.model_dump(), id=1, created_at=now)
    return patient

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)