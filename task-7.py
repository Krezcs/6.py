import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

subject_name = 'Biology'
group_name = 'Group B'

query = f'''
    SELECT st.student_id, st.student_name, g.grade, g.date
    FROM students st
    JOIN grades g ON st.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    WHERE subj.subject_name = '{subject_name}' AND st.group_id = (SELECT group_id FROM groups WHERE group_name = '{group_name}');
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"Grades of students in {subject_name}, {group_name}:")
print("Student ID | Student Name         | Grade | Date")
print("---------------------------------------------------------------")
for row in result:
    student_id, student_name, grade, date = row
    print(f"{student_id:10} | {student_name:20} | {grade:5} | {date}")

conn.close()
