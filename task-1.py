import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

query = '''
    SELECT s.student_id, s.student_name, AVG(g.grade) AS average_grade
    FROM students s
    JOIN grades g ON s.student_id = g.student_id
    GROUP BY s.student_id, s.student_name
    ORDER BY average_grade DESC
    LIMIT 5;
'''

cursor.execute(query)
result = cursor.fetchall()

print("Top 5 students with the highest average grades:")
print("Student ID | Student Name         | Average Grade")
print("-------------------------------------------------")
for row in result:
    student_id, student_name, average_grade = row
    print(f"{student_id:10} | {student_name:20} | {average_grade:13.2f}")

conn.close()
