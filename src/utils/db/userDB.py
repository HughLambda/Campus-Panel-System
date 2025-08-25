import sqlite3
import hashlib
import datetime
from user import User
DB_NAME = "users.db"


#------Guide to User DB------
#initDB()
#registerUser(user);;register before set please
#setUser(user)
#getUser(user)
#deleteUser(user)
#loginUser(user)


def initDB():
    init_db()
def deleteUser(user:User)->bool:
    deleteUser(user.username)
def loginUser(user:User)->bool:
    login_user(user.username,user.password)
def registerUser(user:User)->bool:
    return register_user(user.username, user.password, user.email, user.data)
def getUser(username:str)->User:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, password, email, data FROM users WHERE username=?
    ''', (username,))
    row = cursor.fetchone()
    conn.close()
    return User(row[1],row[2],row[3],row[4])
def setUser(user:User)->bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE users SET password=?, email=?, data=? WHERE username=?
        ''', (user.password, user.email, user.data, user.username))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            data TEXT,
            created_at TEXT NOT NULL
        )
    ''')
    print(conn.execute("PRAGMA max_length").fetchone())
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username, password, email, data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, password, email, data, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, hash_password(password), email, data, datetime.datetime.now().isoformat()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT password FROM users WHERE username=?
    ''', (username,))
    row = cursor.fetchone()
    conn.close()
    if row and row[0] == hash_password(password):
        return True
    return False

def get_user_info(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, username, email, data, created_at FROM users WHERE username=?
    ''', (username,))
    user = cursor.fetchone()
    conn.close()
    return user
def deleteUser(username:str)->bool:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('''
            DELETE FROM users WHERE username=?
        ''', (username,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("register:",register_user("alice", "password123", "alice@example.com", '{"moreData":"ddd"}'))

    print(login_user("alice", "password123"))

    print(get_user_info("alice"))
    print(get_user_info("a"))
    print(getUser("alice").email)
    user = User("alicee2","newpassword","d","{}")
    print(registerUser(user))
    print(setUser(user))