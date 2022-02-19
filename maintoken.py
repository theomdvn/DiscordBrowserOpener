from os import system
from time import sleep
from selenium import webdriver

Token = 'OTMwODQ4NDY5OTQ4Njk0NjE5.Yd72bA.rA9bk4FZQLcb5Kgo0QrNqfItzjw' #str(input("Parse token. : "))
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://discord.com/login')
sleep(1)
driver.execute_script('window.t = "' + Token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
system('cls')
a = True
while a == True:
    print('Successfully connected')
    print('Token used : ' + Token)
    sleep(3)
    system('cls')
    a = input()