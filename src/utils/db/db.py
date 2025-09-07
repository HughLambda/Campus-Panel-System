import sqlite3
import hashlib
import datetime
from .user import User



dbName = "cps.db"



def initDB():
    initUserDB()
    initClassDB()
    initDormDB()
    initGroupDB()
    initHomeworkDB()
    initStudentDB()
    initScoreDB()
    pass


#------user------
#role:id
def initUserDB():
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            phone TEXT,
            data TEXT,
            createdAt TEXT NOT NULL
        )
    ''')
    print(conn.execute("PRAGMA max_length").fetchone())
    conn.commit()
    conn.close()
    pass
def updateUser():
    pass
def deleteUser():
    pass
def loginUser():
    pass
def getUser():
    pass
def registerUser():
    pass
def hashPassword(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
#------student------
def initStudentDB():
    pass
#------homework------
def initHomeworkDB():
    pass
#------group------
def initGroupDB():
    pass
#------dorm------
def initDormDB():
    pass
#------class------
def initClassDB():
    pass
#------score------
def initScoreDB():
    pass