import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

student_name = 'Robert Dyer'
teacher_name = 'Teacher 2'

query = f'''
    SELECT st.student_id, st.student_name, subj.subject_name, t.teacher_name
    FROM students st
    JOIN grades g ON st.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN teachers t ON subj.teacher_id = t.teacher_id
    WHERE st.student_name = '{student_name}' AND t.teacher_name = '{teacher_name}';
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"Courses taught by {teacher_name} to {student_name}:")
print("Student ID |  Student Name        |  Subject Name | Teacher Name")
print("---------------------------------------------------------------")
for row in result:
    student_id, student_name, subject_name, teacher_name = row
    print(f"{student_id:10} | {student_name:20} | {subject_name:13} | {teacher_name}")

conn.close()
