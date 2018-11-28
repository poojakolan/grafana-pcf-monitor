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

    worksheet = workbook.add_worksheet("MAX_APPS_TASKS")
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
    conn.request("GET", "/proxy/accounting_report/system_report/max_apps_and_tasks", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    apps_task_data = response.read()
    conn.close()
    apps_task_data = json.loads(apps_task_data)
    print("apps_task_data "+ str(apps_task_data))
    worksheet.set_row(row, None, bold)
    worksheet.write(row, col, 'App Task Data:')
    worksheet.set_row(row+3, None, bold)
    worksheet.write(row, col, 'Yearly Data')
    worksheet.write(row+5, col,  'Year')
    worksheet.write(row+5, col+1, 'Month')
    worksheet.write(row+5, col+2, 'maximum_concurrent_apps_and_tasks')
    row = row + 7
    col = 0
    firstMonthReport = apps_task_data['monthly_reports'][0] 
    if(firstMonthReport['month'] > 1):
        for i in range(1, firstMonthReport['month'] -1):
            worksheet.write(row, col,     firstMonthReport['year'])
            worksheet.write(row, col + 1, i)
            worksheet.write(row, col + 2, 0)
            row += 1
    for report in apps_task_data['monthly_reports']:
        worksheet.write(row, col,     report['year'])
        worksheet.write(row, col + 1, report['month'])
        worksheet.write(row, col + 2, report['maximum_concurrent_apps_and_tasks'])
        row += 1
    
    worksheet1 = workbook.add_worksheet("TASK_USAGE_API")
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
    conn.request("GET", "/proxy/accounting_report/system_report/task_usages", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    apps_task_data = response.read()
    conn.close()
    apps_task_data = json.loads(apps_task_data)
    print("apps_task_data "+ str(apps_task_data))
    worksheet.set_row(row, None, bold)
    worksheet.write(row, col, 'App Task Data:')
    worksheet.set_row(row+3, None, bold)
    worksheet.write(row, col, 'Yearly Data')
    worksheet.write(row+5, col,  'Month')
    worksheet.write(row+5, col+1, 'Year')
    worksheet.write(row+5, col+2, 'Total task runs')
    worksheet.write(row+5, col+3, 'maximum_concurrent_tasks')
    worksheet.write(row+5, col+4, 'task_hours')
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
            row += 1
    for report in apps_task_data['monthly_reports']:
        worksheet.write(row, col,     report['month'])
        worksheet.write(row, col + 1, report['year'])
        worksheet.write(row, col + 2, report['total_task_runs'])
        worksheet.write(row, col + 3, report['maximum_concurrent_tasks'])
        worksheet.write(row, col + 4, report['task_hours'])
        row += 1
    
    #App Usage Api
    worksheet1 = workbook.add_worksheet("APP_USAGE_API")
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
    worksheet.set_row(row, None, bold)
    worksheet.write(row, col, 'App Usage Data:')
    worksheet.set_row(row+3, None, bold)
    worksheet.write(row, col, 'Yearly Data')
    worksheet.write(row+5, col,  'Month')
    worksheet.write(row+5, col+1,  'Year')
    worksheet.write(row+5, col+2, 'Average App Instances')
    worksheet.write(row+5, col+3, 'Maximum App Instances')
    worksheet.write(row+5, col+4, 'App Instance Hours')
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
            row += 1
    for report in apps_task_data['monthly_reports']:
        worksheet.write(row, col,     report['month'])
        worksheet.write(row, col + 1, report['year'])
        worksheet.write(row, col + 2, report['average_app_instances'])
        worksheet.write(row, col + 3, report['maximum_app_instances'])
        worksheet.write(row, col + 4, report['app_instance_hours'])
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
