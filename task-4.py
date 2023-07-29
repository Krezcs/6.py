import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

query = '''
    SELECT AVG(grade) AS average_grade
    FROM grades;
'''

cursor.execute(query)
result = cursor.fetchone()

average_grade = result[0]
print(f"Average grade across all grades: {average_grade:.2f}")

conn.close()
