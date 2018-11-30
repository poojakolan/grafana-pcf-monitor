import subprocess
import shlex
import json
import datetime
import time
import xlsxwriter
import httplib, urllib
import math
import bitmath

foundry_list = {'sample-foundry':['api.run.pivotal.io', 'Lakshmiredz@gmail.com','Pooja@123','concourse2','ci', "console.run.pivotal.io"]}

timestamp_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H:%M:%S')

workbook = xlsxwriter.Workbook('monthly_report_'+timestamp_str+'.xlsx')
bold = workbook.add_format({'bold': True})

for foundry in foundry_list:
    flist = foundry_list[foundry]
    api = flist[0]
    user = flist[1]
    pwd = flist[2]
    org = flist[3]
    space = flist[4]
    
    #App Usage Api
    worksheet = workbook.add_worksheet("Monthly Usage")
    row = 1
    col = 0
    login_command = 'cf login -a ' + api + ' -u ' + user + ' -p ' + pwd + ' -o ' + org + ' -s ' + space + ' --skip-ssl-validation'
    process = subprocess.Popen(shlex.split(login_command), stdout=subprocess.PIPE)
    login_output = process.communicate()[0]
    print(login_output)
    token_proc = subprocess.Popen(shlex.split('cf oauth-token'), stdout=subprocess.PIPE)
    token = token_proc.communicate()[0]
    token = token.replace("\n", "")
    params = urllib.urlencode({})
    headers = {"Authorization": token}
    conn = httplib.HTTPSConnection(flist[5])
    conn.request("GET", "/proxy/accounting_report/system_report/app_usages", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    apps_task_data = response.read()
    conn.close()
    apps_task_data = json.loads(apps_task_data)
    print("apps_task_data "+ str(apps_task_data))
    conn.request("GET", "/proxy/accounting_report/system_report/max_apps_and_tasks", params, headers)
    response1 = conn.getresponse()
    print(response1.status, response1.reason)
    max_apps_task_data = response1.read()
    max_apps_task_data = json.loads(max_apps_task_data)
    conn.request("GET", "/proxy/accounting_report/system_report/task_usages", params, headers)
    response2 = conn.getresponse()
    print(response2.status, response2.reason)
    apps_task_usage_data = response2.read()
    conn.close()
    apps_task_usage_data = json.loads(apps_task_usage_data)
    worksheet.set_row(row, None, bold)
    worksheet.write(row, col, 'App Usage Data:')
    worksheet.set_row(row+3, None, bold)
    worksheet.write(row, col, 'Yearly Data')
    worksheet.write(row+5, col,  'Month')
    worksheet.write(row+5, col+1,  'Year')
    worksheet.write(row+5, col+2, 'Average Instances')
    worksheet.write(row+5, col+3, 'Max Concurrent')
    worksheet.write(row+5, col+4, 'Apps')
    worksheet.write(row+5, col+5, 'Tasks')
    worksheet.write(row+5, col+6, 'App Instance Hours')
    worksheet.write(row+5, col+7, 'App Instance Apps')
    worksheet.write(row+5, col+8, 'App Instance Tasks')
    row = row + 7
    col = 0
    firstMonthReport = apps_task_data['monthly_reports'][0] 
    if(firstMonthReport['month'] > 1):
        for i in range(1, firstMonthReport['month'] -1):
            worksheet.write(row, col,     i)
            worksheet.write(row, col + 1, firstMonthReport['year'])
            worksheet.write(row, col + 2, 0)
            worksheet.write(row, col + 3, 0)
            worksheet.write(row, col + 4, 0)
            worksheet.write(row, col + 5, 0)
            worksheet.write(row, col + 6, 0)
            worksheet.write(row, col + 7, 0)
            worksheet.write(row, col + 8, 0)
            row += 1
    for j in range(0, len(apps_task_data['monthly_reports'])):
        worksheet.write(row, col,     apps_task_data['monthly_reports'][j]['month'])
        worksheet.write(row, col + 1, apps_task_data['monthly_reports'][j]['year'])
        worksheet.write(row, col + 2, apps_task_data['monthly_reports'][j]['average_app_instances'])
        worksheet.write(row, col + 3, max_apps_task_data['monthly_reports'][j]['maximum_concurrent_apps_and_tasks'])
        worksheet.write(row, col + 4, max_apps_task_data['monthly_reports'][j]['maximum_concurrent_apps_and_tasks'])
        worksheet.write(row, col + 6, apps_task_usage_data['monthly_reports'][j]['task_hours'])
        worksheet.write(row, col + 5, apps_task_data['monthly_reports'][j]['app_instance_hours'])
        worksheet.write(row, col + 7, apps_task_data['monthly_reports'][j]['app_instance_hours'])
        worksheet.write(row, col + 8, apps_task_usage_data['monthly_reports'][j]['task_hours'])
        apps_task_usage_data
        row += 1
workbook.close()

filename = 'monthly_report_'+timestamp_str+'.xlsx'
fromaddr = ''
toaddr = ''
subject = ''
body = ''
cmd = 'echo '+body+' | mail -s '+subject+' -r '+fromaddr+' -a '+filename+' '+toaddr
send=subprocess.call(cmd,shell=True)

#remove file
process3 = subprocess.Popen(shlex.split('rm '+filename), stdout=subprocess.PIPE)
stdout3 = process3.communicate()[0]
print(stdout3)
