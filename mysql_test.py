import mysql.connector

import time    
time.strftime('%Y-%m-%d %H:%M:%S')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="grafana"
)

mycursor = mydb.cursor()

org = 'ci-org'
#sql = ("INSERT INTO pcf_org (id, org_name) VALUES (%d, %s)")
sql2 = ("SELECT id FROM pcf_org WHERE org_name = %s")
sql = ("INSERT INTO pcf_org "
               "(id, org_name) "
               "VALUES (%s, %s)")


insert_org_sql = ("INSERT INTO pcf_org "
               "(org_name, foundry_id, memory_consumption_percent, last_updated) "
               "VALUES (%s, %s, %s, %s)")

val = (12, "test_org")
val2 = ('ci-org')
val_org_insert = ('test_org', 2, 0, time.strftime('%Y-%m-%d %H:%M:%S'))
#mycursor.execute(sql2)

mycursor.execute(insert_org_sql, val_org_insert)

'''rows = mycursor.fetchall()
 
print('Total Row(s):', mycursor.rowcount)
for row in rows:
    print(row)'''

#print(mycursor.rowcount, "record inserted.")


mydb.commit()