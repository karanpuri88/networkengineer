import requests
import json

vManage_ip = input("Please Enter IP address of vManage : ")
username = input("Please enter vManage's Username : ")
password = input("Please enter vManage Password : ")

# GENERATE SESSION COOKIES (J-SESSION ID)
def generate_cookies():
    global cookie
    url = "https://%s:8443/j_security_check"%(vManage_ip)
    payload = {"j_username" : username , "j_password" : password}
    sess = requests.session()
    response = sess.post(url, data = payload, verify=False)
    for out in response.cookies:
        cookie = out.name + "=" + out.value

# GENERATE THE TOKEN USING COOKIES
def generate_token():
    global real_token
    token_url = "https://%s:8443/dataservice/client/token?json=true"%(vManage_ip)
    headers = {'Cookie' : cookie,'Accept' : 'application/json'}
    get_token = requests.get(token_url, headers=headers, verify=False)
    real_token = get_token.json()["token"]

# PERFORM API CALL USING BOTH SESSION & TOKEN ID
def api_call():
    device_ip = input("Please enter Edge IP : ")
    api = input("Enter the API url : ")
    # api = "dataservice/device/arp"
    generate_cookies()
    generate_token()
    api_url = "https://%s:8443/%s?deviceId=%s"%(vManage_ip,api,device_ip)
    data = {'Cookie' : cookie,'X-XSRF-TOKEN' : real_token, 'Content-Type' : 'application/json','Accept' : 'application/json'}
    output = requests.get(api_url, headers=data, verify=False)
    result = output.content
    return result

# STORE RESULT & BEAUTIFY JSON FORMAT
final = api_call()
json_object = json.loads(final)
print(json.dumps(json_object, indent=4))