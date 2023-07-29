import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

group_name = 'Group A'

query = f'''
    SELECT student_id, student_name
    FROM students
    WHERE group_id = (SELECT group_id FROM groups WHERE group_name = '{group_name}');
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"List of students in {group_name}:")
print("Student ID | Student Name")
print("-----------------------------------")
for row in result:
    student_id, student_name = row
    print(f"{student_id:10} | {student_name}")

conn.close()
