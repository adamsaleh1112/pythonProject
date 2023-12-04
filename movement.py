import requests
from datetime import datetime

from login import returnName

def forward():
    url = 'http://192.168.1.21:5000/forward'
    data = {'command': 'forward'}
    response = requests.post(url, data=data)

    global name
    name = returnName()

    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(name + ': ' + dt_string + ' Move forward \n')

def backward():
    url = 'http://192.168.1.21:5000/backward'
    data = {'command': 'backward'}
    response = requests.post(url, data=data)
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string + ' Move backward \n')

def left():
    url = 'http://192.168.1.21:5000/left'
    data = {'command': 'left'}
    response = requests.post(url, data=data)
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string + ' Move left \n')

def right():
    url = 'http://192.168.1.21:5000/right'
    data = {'command': 'right'}
    response = requests.post(url, data=data)
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string + ' Move right \n')

def stop():
    url = 'http://192.168.1.21:5000/stop'
    data = {'command': 'stop'}
    response = requests.post(url, data=data)
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string + ' Move stop \n')

def go():
    url = 'http://192.168.1.21:5000/go'
    data = {'command': 'go'}
    response = requests.post(url, data=data)
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(dt_string + ' Move go \n')
