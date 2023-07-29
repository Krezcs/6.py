import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

subject_name = 'Mathematics'

query = f'''
    SELECT s.student_id, s.student_name, AVG(g.grade) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    WHERE subj.subject_name = '{subject_name}'
    GROUP BY s.student_id, s.student_name
    ORDER BY average_grade DESC
    LIMIT 1;
'''

cursor.execute(query)
result = cursor.fetchone()

if result:
    student_id, student_name, average_grade = result
    print(f"Student with the highest average grade in {subject_name}:")
    print("Student ID | Student Name         | Average Grade")
    print("-------------------------------------------------")
    print(f"{student_id:10} | {student_name:20} | {average_grade:13.2f}")
else:
    print(f"No students found for the subject: {subject_name}")

conn.close()
