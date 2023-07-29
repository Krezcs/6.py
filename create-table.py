import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE groups (
        group_id INTEGER PRIMARY KEY,
        group_name VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE students (
        student_id INTEGER PRIMARY KEY,
        student_name VARCHAR(100) NOT NULL,
        group_id INT,
        FOREIGN KEY (group_id) REFERENCES groups (group_id)
    )
''')

cursor.execute('''
    CREATE TABLE teachers (
        teacher_id INTEGER PRIMARY KEY,
        teacher_name VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name VARCHAR(100) NOT NULL,
        teacher_id INT,
        FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id)
    )
''')

cursor.execute('''
    CREATE TABLE grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INT,
        subject_id INT,
        grade INT NOT NULL CHECK (grade >= 1 AND grade <= 100),
        date DATE NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    )
''')

conn.commit()
conn.close()
