import csv
from os import system
from time import sleep
from turtle import bgcolor
from selenium import webdriver
from platform import python_branch
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time


TOKEN_LIST = list()
PROXY_LIST = list()
proxy = list()
proxy_used = ''
DRIVERS = list()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

with open('DiscordOpener.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        TOKEN_LIST.append(line[2])
        try:
            proxy = line[3].split(':')
            formated_proxy = f"{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}"
            PROXY_LIST.append(formated_proxy)
            DRIVERS.append(f'drivers{line}')
        except:
            print('Veuillez remplir le csv')

i=0
for Token in TOKEN_LIST:
    proxy_used = PROXY_LIST[i]
    options = {
    'proxy': {
        'http': f'http://{proxy_used}',
        'https': f'http://{proxy_used}',
        'no_proxy': 'localhost,127.0.0.1'
        }
    }
    DRIVERS[i] = webdriver.Chrome(seleniumwire_options=options)
    #DRIVERS[i].maximize_window()
    DRIVERS[i].get('https://discord.com/login')
    sleep(1)
    DRIVERS[i].execute_script('window.t = "' + Token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
    system('cls')
    print(bcolors.OK + 'Successfully connected' + bcolors.RESET)
    print(bcolors.WARNING + 'Token used : ' + Token)
    print('Proxy used : ' + proxy_used + bcolors.RESET)
    sleep(3)
    system('cls')

    if i == TOKEN_LIST.__len__()-1:
        print(bcolors.OK + 'All account have been logged in' + bcolors.RESET)
        input(bcolors.WARNING + 'Press enter to close all browsers' + bcolors.RESET)
    else:
        print(bcolors.WARNING + '10 secondes before next browser...' + bcolors.RESET)
        i=i+1
    time.sleep(10)
