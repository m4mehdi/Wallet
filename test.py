import requests
import pytest
import json

url ='http://127.0.0.1:8000/api'

def test_add_money(userID):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({'amount':100})
    addmoney = url + '/add-money/' + str(userID)
    response = requests.post(url=addmoney, data=data, headers=headers)
    if response.status_code == 200:
        print('\n add-money works')

def test_get_balance(userID):
    balance = url + '/get-balance/' + str(userID)
    response = requests.get(url=balance)

    if response.status_code == 200:
        print('\n get-balance works')

def test_wallet_not_exist(userID):
    balance = url + '/get-balance/' + str(userID)
    response = requests.get(url=balance)

    if response.status_code == 400:
        print('\n True result for not existing wallet')
def test_amount_int_check(userID):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({'amount':'100'})
    addmoney = url + '/add-money/' + str(userID)
    response = requests.post(url=addmoney, data=data, headers=headers)
    if response.status_code == 400:
        print('\n True result for not int amount')

def test_true_add(userID,amount):
    balance = url + '/get-balance/' + str(userID)
    response = requests.get(url=balance)
    total1 = response.json()['total']
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({'amount':amount})
    addmoney = url + '/add-money/' + str(userID)
    requests.post(url=addmoney, data=data, headers=headers)

    response = requests.get(url=balance)
    total2 = response.json()['total']
    if (total2-total1 == amount):
        print('\n True add to user wallet')


#1--Add Money
print('\n Test 1 === Add money')
test_add_money(1)

#2--Get Balance
print('\n Test 2 === Get balance')
test_get_balance(1)

#3--Not Existing Wallet
print('\n Test 3 === Not existing balance')
test_wallet_not_exist(20)

#4--Not int money
print('\n Test 4 === Not int money check')
test_amount_int_check(2)

#4--Check add money to wallet
print('\n Test 5 === Check true add money to user wallet')
test_true_add(1,300)

#5--Check minus money to wallet
print('\n Test 6 === Check true minus money to user wallet')
test_true_add(1,-200)
