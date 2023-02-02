import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="toor",
    database="employees"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM departments")
result = cursor.fetchall()
result2 = result[1]
print(result2[1])
cursor.close()
conn.close()