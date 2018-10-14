import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="grafana"
)

mycursor = mydb.cursor()

org = 'ci-org'
#sql = ("INSERT INTO pcf_org (id, org_name) VALUES (%d, %s)")
sql = ("INSERT INTO pcf_org "
               "(org_name) "
               "VALUES (%s)")
val = ("test_org1",)
#mycursor.execute(sql2)

mycursor.execute(sql, val)

print(mycursor.lastrowid)

print(mycursor.rowcount, "record inserted.")

mydb.commit()