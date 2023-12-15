import psycopg2
import model
import helper

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
        cur.execute("SELECT * FROM doctors")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

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