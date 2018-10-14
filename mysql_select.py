import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="grafana"
)

mycursor = mydb.cursor()
org = 'ci-org1'
sql = "SELECT id FROM pcf_org WHERE org_name = %s"
adr = (org, )

mycursor.execute(sql, (org,))

myresult = mycursor.fetchall()
print(len(myresult))
if(len(myresult) == 1):
    print('found value', myresult[0][0])

for x in myresult:
  print(x[0])