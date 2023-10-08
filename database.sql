-- SQL script to create database schema for app
CREATE DATABASE IF NOT EXISTS med_craft;
--- table name : med_carft_users.
CREATE TABLE IF NOT EXISTS med_craft_users(user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    username VARCHAR(200) NOT NULL, 
    firstname VARCHAR(100) NOT NULL, 
    middle_name VARCHAR(100), 
    lastname VARCHAR(100), 
    password VARCHAR(100) NOT NULL, 
    access_token VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    phone VARCHAR(100) NOT NULL, 
    is_active INT NOT NULL DEFAULT 1,  
    created_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, 
    update_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL);
--- table name : organizations.
CREATE TABLE IF NOT EXISTS organizations(organization_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    org_name VARCHAR(200) NOT NULL, 
    org_address TEXT NOT NULL, 
    org_country VARCHAR(100) NOT NULL, 
    org_state VARCHAR(100) NOT NULL, 
    org_city VARCHAR(100) NOT NULL, 
    is_active TINYINT(1) NOT NULL DEFAULT 1, 
    creation_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, 
    updated_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
    phone VARCHAR(20) NOT NULL, email VARCHAR(20) NOT NULL, 
    passwd TEXT NOT NULL);
--- table name: doctors.
-- table name : hospital.
CREATE TABLE IF NOT EXISTS hospital(hospital_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    hospital_name VARCHAR(200) NOT NULL, 
    hospital_addr TEXT NOT NULL, 
    phone VARCHAR(20) NOT NULL, 
    organizations_id INT);
-- table name: patient.
CREATE TABLE IF NOT EXISTS patients(
    patient_id INT PRIMARY KEY, 
    patient_name VARCHAR(200) NOT NULL, 
    patient_addr VARCHAR(200) NOT NULL, 
    phone VARCHAR(20) NOT NULL);

CREATE TABLE IF NOT EXISTS doctors(
    doctor_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    organization_id INT NOT NULL, 
    hospital_id INT, fullname VARCHAR(200) NOT NULL, 
    email VARCHAR(200) NOT NULL, 
    phone VARCHAR(20) NOT NULL)
ALTER TABLE hospital ADD COLUMN hospital_password VARCHAR(20);
ALTER TABLE hospital ADD COLUMN hospital_access_token TEXT;

CREATE TABLE IF NOT EXISTS patient_details (
    patient_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    patient_name VARCHAR(100),
    patient_address TEXT,
    patient_phone VARCHAR(1000),
    organization_id VARCHAR(1000),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE IF NOT EXISTS patient_appointment (
    patient_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    doctor_name VARCHAR(100),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)