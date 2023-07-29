import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

teacher_name = 'Teacher 1'

query = f'''
    SELECT t.teacher_name, s.subject_name
    FROM teachers t
    JOIN subjects s ON t.teacher_id = s.teacher_id
    WHERE t.teacher_name = '{teacher_name}';
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"Courses taught by {teacher_name}:")
print("Teacher Name | Subject Name")
print("---------------------------")
for row in result:
    teacher_name, subject_name = row
    print(f"{teacher_name:12} | {subject_name}")

conn.close()
