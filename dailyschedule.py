import schedule
import time
import datetime
import requests
import pytest
import json

url ='http://127.0.0.1:8000/api'
def get_dailytransactions():
    dailytransactions = url + '/daily-transactions'
    response = requests.get(url=dailytransactions)
    return response

def job():
    response = get_dailytransactions()
    print("Total Daily Transaction is = ", response.json()['total'])

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
