import mysql.connector

#conn = mysql.connector.connect(username='root', password='@omama1234',host='localhost',database='face_recognition',port=3307)
conn = mysql.connector.connect(host="localhost",user="root",password="@omama1234",database="face_recognition",port=3307)
if conn.is_connected () == False:
    print("Database not Conneted")
cursor = conn.cursor()
cursor.execute("show databases")
data = cursor.fetchall()
print(data)
conn.close()