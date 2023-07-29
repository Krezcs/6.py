import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

student_name = 'Jessica Baker'

query = f'''
    SELECT st.student_id, st.student_name, subj.subject_name
    FROM students st
    JOIN grades g ON st.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    WHERE st.student_name = '{student_name}';
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"Courses attended by {student_name}:")
print("Student ID | Student Name         | Subject Name")
print("-------------------------------------------------------")
for row in result:
    student_id, student_name, subject_name = row
    print(f"{student_id:10} | {student_name:20} | {subject_name}")

conn.close()
