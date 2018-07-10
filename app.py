import gspread
from oauth2client.service_account import ServiceAccountCredentials
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests
import gspread

import schedule
import time
DATE = 0
def job():
    print("I'm working...")
    global DATE
    DATE += 1
    url = 'https://notify-api.line.me/api/notify'
    token = 'NeVGMudOdPmNcZ3nRWP1HtTzeM8O95gZPEzEvMlY2vt'
    headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('LINE PM-fe2ce7fab2c8.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1St8Cv7PP2b5Qe02n2TSDnd_XcjRO8Eoyjbt0ASraUQw')
    ws = wks.get_worksheet(0)
    val = ws.acell('A'+str(DATE)).value
    print val
    print DATE

    msg = val
    r = requests.post(url, headers=headers , data = {'message':msg})
    print r.text
    
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    

