import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

teacher_name = 'Teacher 3'

query = f'''
    SELECT t.teacher_name, AVG(g.grade) AS average_grade
    FROM teachers t
    JOIN subjects s ON t.teacher_id = s.teacher_id
    JOIN grades g ON s.subject_id = g.subject_id
    WHERE t.teacher_name = '{teacher_name}'
    GROUP BY t.teacher_name;
'''

cursor.execute(query)
result = cursor.fetchone()

if result:
    teacher_name, average_grade = result
    print(f"Average grade given by {teacher_name}: {average_grade:.2f}")
else:
    print(f"No data found for {teacher_name}")

conn.close()
