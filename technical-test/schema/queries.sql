CREATE DATABASE zicare_clinic;

-- Data Insertion

CREATE TABLE IF NOT EXISTS patients (
    id SERIAL PRIMARY KEY,
    phone VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
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

-- Data Population

INSERT INTO specialities (name, description) 
VALUES 
    ('Sp. THT', 'Telinga, hidung, dan tenggorokan'), 
    ('Sp. Anak', 'Kesehatan anak');

INSERT INTO doctors (speciality_id, first_name, middle_name, last_name, birth_date, joined_at)
VALUES
    (1, 'Foo', 'Bar', 'Baz', '1970-01-01', '2020-01-01'),
    (2, 'Nirina', 'Raudhatul', 'Zubir', '1980-03-12', '2019-01-01'); 