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
    
    

# Define the URL and payload (parameters)


headers1 = {
    'Host': 'bnbfree.in',
    'Accept': '*/*',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Csrf-Token':'null',
    'Cookie': '_ga=GA1.1.100534944.1706440996; csrf_token=9fwe538ZpwYT; connect.sid=s%3Ax5L7WUfIgcweYfAPKQlNhKAk0d6juGo9.jd2oFHhkVmYG%2Fhl35IOa8aKLRkVWSftePb2atzhPgxc; btc_address=123; password=123; fbtc_userid=123; fbtc_session=123; have_account=1; mobile=1; _ga_7W471KHZG7=GS1.1.1706454565.2.1.1706454598.0.0.0',
    
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'X-Request-With':'XMLHttpRequest'
}

# Make the GET request with the payload

    	
    
#csrf = 
email = '1fad3fde0dc3279a86f55e445c824847'
pas = 'iEjoup0bY4chRj8p'
fv2 = '1760875237'

url1 = 'https://bnbfree.in'
api = Api_MB()
data = {"method": "hcaptcha", "pageurl": "https://bnbfree.in/", "sitekey": "2ca356f0-8121-44d8-9596-6aeb24529e95"}

while True:
    # Perform the CAPTCHA solving and POST request
    cap = api.run(data)
    claim_payload = f"csrf_token=&op=free_play&fingerprint={email}&client_seed={pas}&fingerprint2={fv2}&pwc=0&h_recaptcha_response={cap}"
    response = requests.post(url1, data=claim_payload, headers=headers1)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the desired values from the response
        s = str(response.text)
        parts = s.split(":")
        if len(parts) >= 4:  # Ensure there are enough parts to extract
            extracted_substring = ":".join(parts[1:4])
            subparts = extracted_substring.split(":")
            a = subparts[0]
            b = subparts[1]
            c = subparts[2]
            print(f"roll number={a},  Balance={b}, Reward={c}")
        else:
            print("Unexpected response format")
    else:
        print(f"Request failed with status code {response.status_code}")
    
    # Wait for a random time before the next iteration
    wait(random.randint(3600, 3672))
