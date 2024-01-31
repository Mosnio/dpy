import requests
from bs4 import BeautifulSoup
import requests,random,json
import time,sys,subprocess,re
from datetime import datetime

import requests
import json,os
import time,sys
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import time,random
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import datetime
import os
import sys
import json
import time
import random
import requests
import datetime
from colorama import Fore, Back, Style, init
from random import randint
import requests
from fake_useragent import UserAgent
import random

# Create an instance of UserAgent
ua = UserAgent()
import os
init(autoreset=True)

sc_ver = "CLAIMBTC.ONLINE v5"

end = "\033[K"
res = Style.RESET_ALL
red = Style.BRIGHT+Fore.RED
bg_red = Back.RED
white = Style.BRIGHT+Fore.WHITE
green = Style.BRIGHT+Fore.GREEN
yellow = Style.BRIGHT+Fore.YELLOW
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]


def wait(x):
    for i in range(x, -1, -1):
        col = yellow if i % 2 == 0 else white
        animation = "⫸" if i % 2 == 0 else "⫸⫸"
        m, s = divmod(i, 60)
        t = f"[00:{m:02}:{s:02}]"
        sys.stdout.write(f"\r  {white}Please wait {col}{t} {animation}{res}{end}\r")
        sys.stdout.flush()
        time.sleep(1)
        
        
def Session():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

class Api_MB:
    def __init__(self):
        self.url = "http://api.multibot.in"
        self.key = "5Z4sWvudz6Jjfw2nK10YcOFkRbQVMU"
        self.max_wait = 300
        self.sleep = 5

    def in_api(self, data):
        session = Session()
        params = {"key": (None, self.key), "json": (None, "1")}
        for key in data:
            params[key] = (None, data[key])
        return session.post(self.url + '/in.php', files=params, verify=False, timeout=5)

    def res_api(self, api_id):
        session = Session()
        params = {"key": self.key, "id": api_id, "json": "1"}
        return session.get(self.url + '/res.php', params=params, verify=False, timeout=5)

    def run(self, data):
        get_in = self.in_api(data)
        if get_in:
            if json.loads(get_in.text)['status']:
                api_id = json.loads(get_in.text)['request']
            else:
                return json.loads(get_in.text)['request']
        else:
            return "WRONG_RESPONSE_API"
        for i in range(self.max_wait//self.sleep):
            time.sleep(self.sleep)
            get_res = self.res_api(api_id)
            if get_res:
                answer = json.loads(get_res.text)['request']
                if 'CAPCHA_NOT_READY' in answer:
                    continue
                else:
                    return answer
                    
                    

def msg_line():
 #   green = "\033[92m"  # ANSI escape code for green color
    print(f"{green}{'━' * 50}")
    

url = 'https://freeth.in'

ua = UserAgent()

# Define the login headers with a random User-Agent
login_headers = {
    'Host': 'freeth.in',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': ua.random,  # Use ua.random to get a random User-Agent string
    'X-Requested-With': 'XMLHttpRequest'
}




api = Api_MB()
data = {"method": "hcaptcha", "pageurl": "https://freeth.in/", "sitekey": "50a93309-7138-4f50-8a5f-420eb5f9b2ce"}
cap = api.run(data)

signup_payload = {
    'csrf_token': '',
    'op': 'signup_new',
    'password': 'pUoUn2gdlZ',
    'email': 'sharon.smith@gmail.com','fingerprint':'1fad3fde0dc3279a86f55e445c824847',
    'referrer':'17082',
    'h_recaptcha_response':cap
}

response = requests.post(url, data=signup_payload,headers=login_headers)

print(response.text)
