import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DB!code#2026"
)

cursor = conn.cursor(dictionary=True)

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS doubt_resolution_platform")

# Use database
cursor.execute("USE doubt_resolution_platform")

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100),
email VARCHAR(100),
phone VARCHAR(20),
education VARCHAR(100),
skill VARCHAR(100),
password VARCHAR(255)
)
""")

# Chats table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INT AUTO_INCREMENT PRIMARY KEY,
sender VARCHAR(100),
receiver VARCHAR(100),
message TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Skills table
cursor.execute("""
CREATE TABLE IF NOT EXISTS skills(
id INT AUTO_INCREMENT PRIMARY KEY,
skill_name VARCHAR(100),
title VARCHAR(255),
link TEXT
)
""")

# Connections table
cursor.execute("""
CREATE TABLE IF NOT EXISTS connections(
id INT AUTO_INCREMENT PRIMARY KEY,
user1 VARCHAR(100),
user2 VARCHAR(100),
status VARCHAR(50),
request_type VARCHAR(50)
)
""")

conn.commit()
conn.close()

print("MySQL Database created successfully")