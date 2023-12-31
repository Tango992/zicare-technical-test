from fastapi import HTTPException
from typing import List
import model
import psycopg2

conn = psycopg2.connect(
    database="zicare",
    host="host.docker.internal",
    user="postgres",
    password="secret", 
    port="5432"
)
conn.autocommit = True


def get_all_doctors() -> List[model.Doctor]:
    try:
        cur = conn.cursor()
        cur.execute("SELECT d.id, s.name, CONCAT(d.first_name, ' ', d.middle_name, ' ', d.last_name) AS full_name FROM doctors d JOIN specialities s ON d.speciality_id = s.id")
        row = cur.fetchone()
        doctors = []
        
        while row is not None:
            doctor = model.Doctor(id= row[0], speciality=row[1], full_name=row[2])
            doctors.append(doctor)
            row = cur.fetchone()

        return doctors

    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})
    

def register_patient(patient: model.RegisterPatient) -> int:
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO patients (phone, password, first_name, middle_name, last_name, birth_date) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id", (patient.phone, patient.password, patient.first_name, patient.middle_name, patient.last_name, patient.birth_date))
        row = cur.fetchone()
        return row[0]
        
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})
    

def get_patient_password_by_phone(phone) -> str:
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT password FROM patients WHERE phone = '{phone}'")
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})
    

def get_patient_id_by_phone(phone) -> int:
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM patients WHERE phone = '{phone}'")
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})
    

def create_appointment(data: model.AppointmentRequest) -> int:
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO reservations (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s,%s,%s,%s) RETURNING id", (data.patient_id, data.doctor_id, data.appointment_date, data.appointment_time))
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})
    

def find_user_appointments(user_id: int) -> List[model.Appointment]:
    try:
        cur = conn.cursor()
        query = f"SELECT id, patient_id, doctor_id, CAST(appointment_date AS TEXT), CAST(appointment_time AS TEXT) FROM reservations WHERE patient_id = {user_id}"
        cur.execute(query)
        row = cur.fetchone()
        appointments = []
        
        while row is not None:
            appointment = model.Appointment(
                queue_id=row[0],
                patient_id=row[1],
                doctor_id=row[2],
                appointment_date=row[3],
                appointment_time=row[4],
            )
            appointments.append(appointment)
            row = cur.fetchone()

        return appointments

    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})


def delete_user_appointment(queue_id: int, user_id:int) -> int:
    try:
        cur = conn.cursor()
        query = f"DELETE FROM reservations WHERE id = {queue_id} AND patient_id = {user_id}"
        cur.execute(query)
        return cur.rowcount
    
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})


def update_user_appointment(data: model.Appointment) -> int:
    try:
        cur = conn.cursor()
        query = f"UPDATE reservations SET doctor_id = {data.doctor_id}, appointment_date = '{data.appointment_date}', appointment_time = '{data.appointment_time}' WHERE id = {data.queue_id} AND patient_id = {data.patient_id}"
        cur.execute(query)
        return cur.rowcount
    
    except (Exception, psycopg2.DatabaseError) as error:
        raise HTTPException(status_code=400, detail={"error": f"{error}"})