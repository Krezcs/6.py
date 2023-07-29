import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

subject_name = 'Physics'

query = f'''
    SELECT st.group_id, g.group_name, AVG(g.grade) AS average_grade
    FROM students st
    JOIN grades g ON st.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN groups g ON st.group_id = g.group_id
    WHERE subj.subject_name = '{subject_name}'
    GROUP BY st.group_id, g.group_name;
'''

cursor.execute(query)
result = cursor.fetchall()

print(f"Average grade for each group in {subject_name}:")
print("Group ID | Group Name | Average Grade")
print("--------------------------------------")
for row in result:
    group_id, group_name, average_grade = row
    print(f"{group_id:8} | {group_name:10} | {average_grade:13.2f}")

conn.close()
