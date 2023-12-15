import psycopg2
import model

conn = psycopg2.connect(
    database="zicare",
    host="localhost",
    user="postgres",
    password="secret", 
    port="5432"
)
conn.autocommit = True

def get_all_doctors():
    try:
        cur = conn.cursor()
        cur.execute("SELECT d.id, s.name, CONCAT(d.first_name, ' ', d.middle_name, ' ', d.last_name) AS full_name FROM doctors d JOIN specialities s ON d.speciality_id = s.id")
        row = cur.fetchone()
        doctors = []
        
        while row is not None:
            print(row)
            doctor = model.Doctor(id= row[0], speciality=row[1], full_name=row[2])
            doctors.append(doctor)
            row = cur.fetchone()

        return doctors

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            

def register_patient(patient: model.RegisterPatient):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO patients (phone, password, first_name, middle_name, last_name, birth_date) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id", (patient.phone, patient.password, patient.first_name, patient.middle_name, patient.last_name, patient.birth_date))
        row = cur.fetchone()
        return row[0]
        
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)

def get_patient_password_by_phone(phone):
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT password FROM patients WHERE phone = '{phone}'")
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_patient_id_by_phone(phone):
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM patients WHERE phone = '{phone}'")
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def create_appointment(data: model.AppointmentRequest):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO reservations (patient_id, doctor_id, appointment_date, appointment_time) VALUES (%s,%s,%s,%s) RETURNING id", (data.patient_id, data.doctor_id, data.appointment_date, data.appointment_time))
        result = cur.fetchone()
        return result[0]
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
