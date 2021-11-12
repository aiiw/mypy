import requests,json
from urllib.parse import  quote,unquote

session = requests.Session()


form_data = {
    "ReturnUrl": "/",
    "ValidateCodeID": "",
    "Login": "11608",
    "Password": "!@12qwaszx",
    "ValidateCode": 1,
    "RememberMe": 1,
}

i2 = session.post('http://192.168.0.181:8090/Authentication/Validate', data=form_data)
c2 = i2.cookies.get_dict()
print(i2)

