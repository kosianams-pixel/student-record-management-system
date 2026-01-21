import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            level TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_student(name, department, level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, department, level) VALUES (?, ?, ?)",
        (name, department, level)
    )
    conn.commit()
    conn.close()

def get_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(student_id, name, department, level):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, department=?, level=? WHERE id=?",
        (name, department, level, student_id)
    )
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
