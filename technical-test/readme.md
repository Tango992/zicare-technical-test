# Readme

## Task

1. Design Schema for the following:
List of Patients, each patient can do a reservation for a consultation, the reservation is based on the clinic slot/schedule
patient will get the queueing number

2. Architecture Test:
using python with Fastapi framework.
Based on your schema, write CRUD APIs for the patient reservation case

You can either submit
the Github link or zip folder. Write any assumptions that you have in README.md

Some things that we’d like to see on the project:

- Explanation of your project structure or design pattern that you implement
- Short manual to run the application (+ with docker, a must if you are not using python with fastapi framework)
- API documentation. You can choose any format you like
including README.md

## Schema

![Database Schelma](./schema/zicare_clinic_schema.svg)

## Instruction

### Create and Populate the Database

Create a new database

```sql
CREATE DATABASE zicare_clinic;
```

Create tables and relationships

```sql
CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    birth_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS specialities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS doctors (
    id SERIAL PRIMARY KEY,
    speciality_id INT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    last_name VARCHAR(255),
    birth_date DATE NOT NULL,
    joined_at DATE NOT NULL,
    is_active BOOLEAN NOT NULL,
    FOREIGN KEY(speciality_id) REFERENCES specialities(id)
);

CREATE TABLE IF NOT EXISTS doctor_backgrounds (
    id SERIAL PRIMARY KEY,
    doctor_id INT NOT NULL,
    degree VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);

CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    FOREIGN KEY(patient_id) REFERENCES patients(id),
    FOREIGN KEY(doctor_id) REFERENCES doctors(id)
);

CREATE TABLE IF NOT EXISTS medicines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    ingredients VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS prescriptions (
    id SERIAL PRIMARY KEY,
    reservation_id INT NOT NULL,
    medicine_id INT NOT NULL,
    quantity INT NOT NULL,
    notes VARCHAR(255),
    FOREIGN KEY(reservation_id) REFERENCES reservations(id),
    FOREIGN KEY(medicine_id) REFERENCES medicines(id)
);
```