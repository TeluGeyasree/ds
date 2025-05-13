import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Root",database="mecscsd")
if connection.is_connected():
    print("Connected to mysql")
cursor=connection.cursor()
insert_query="INSERT INTO student(sno,name,rollno,marks)VALUES(%s,%s,%s,%s)"
student_data=(1,"kaushik",2000,101)
cursor.execute(insert_query,student_data)
connection.commit()
