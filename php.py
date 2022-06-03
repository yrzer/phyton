import mysql.connector

connection=mysql.connector.connect(user='epiz_31833756',password='Szczepek21',host='sql113.epizy.com',database='epiz_31833756_chat',port='3306')
query='SELECT * FROM osoby'
cursor=connection.cursor().execute(query)
for row in cursor:
  print(row)