import subprocess
import shlex
import json
import datetime
import time
import xlsxwriter
import httplib, urllib
import math
import bitmath
import mysql.connector

timestamp_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')
health_watch_url = "healthwatch.hdc2.cloud.8451.com"

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="grafana"
)

#mycursor = db.cursor()
#mycursor.execute(update_app_historic, ("H",))
#mycursor.execute(update_foundry_historic, ("H",))
#db.commit()
params = urllib.urlencode({})
headers = {}
conn = httplib.HTTPSConnection(health_watch_url)
conn.request("GET", "/panels/diego", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()
print(data)
#json_stats = json.loads(data)
#print(json_stats)
