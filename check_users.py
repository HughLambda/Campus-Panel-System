import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Retrieve all users
cursor.execute('SELECT id, username, password, email, data FROM users')
users = cursor.fetchall()

print("Users in database:")
for user in users:
    print(f"ID: {user[0]}, Username: {user[1]}, Password (hashed): {user[2]}, Email: {user[3]}, Data: {user[4]}")
    
conn.close()