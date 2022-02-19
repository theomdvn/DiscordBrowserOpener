from wsgiref import headers
import requests
import json
import time
import os
def join(link):

    headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US", 
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
    r = requests.post(f"https://discord.com/api/v9/invites/{link}", headers=headers)
    if r.status_code == 200:
        print(f'Success joining discord : discord.gg/{link}')
        time.sleep(10)
    else:
        print(f'Error joining discord: {r.status_code}')
        time.sleep(10)

def get_message(channelid,messageid):
    headers = {
            "Authorization": token,
            "accept": "*/*",
            "accept-language": "en-US", 
            "connection": "keep-alive",
            "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT": "1",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "referer": "https://discord.com/channels/@me",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
    #r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages/{messageid}', headers=headers)
    r = requests.put('https://discord.com/api/v9/channels/930855221217878036/messages/936378666588438589/reactions/%E2%9C%85/%40me', headers=headers)
    if r.status_code == 200:
        print(f'Got message')
        json_ = json.load(r.text)
        print(json_)
        time.sleep(10)
    else:
        print(f'Error getting message : {r.status_code}')
        time.sleep(10)


#https://discord.com/api/v9/channels/930855221217878036/messages/936375859483381852/reactions/%F0%9F%91%80/%40me

token = "OTMwODQ4NDY5OTQ4Njk0NjE5.Yd72bA.rA9bk4FZQLcb5Kgo0QrNqfItzjw"
#invite_link = 'rn7q5Fyq'
channel_id = '930855221217878036'
message_id = '936375859483381852'

#join(invite_link)
get_message(channel_id,message_id)

