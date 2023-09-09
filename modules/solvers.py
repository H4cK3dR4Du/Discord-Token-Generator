import httpx
import time
import json
import requests

def payload(service:str="capsolver.com", proxy:str=None, user_agent:str=None) -> None:
    config = json.loads(open('config.json', 'r').read())
    key = config['captcha_keys']['capsolver']
    p = {
        "clientKey": key,
        "task": {
            "websiteURL":"https://discord.com/",
            "websiteKey":"4c672d35-0701-42b2-88c3-78380b0db560",
        }
    }
    if service == "capsolver.com": 
        p['appId']="E68E89B1-C5EB-49FE-A57B-FBE32E34A2B4"
        p['task']['type'] = "HCaptchaTurboTask"
        p['task']['proxy'] = proxy 
        p['task']['userAgent'] = user_agent
    if service == "capmonster.cloud": 
        p['task']['type'] = "HCaptchaTask"
        p['task']['proxyType'] = "http"
        p['task']['proxyAddress'] = proxy.split("@")[1].split(":")[0]
        p['task']['proxyPort'] = proxy.split("@")[1].split(":")[1]
        p['task']['proxyLogin'] = proxy.split("@")[0].split(":")[0]
        p['task']['proxyPassword'] = proxy.split("@")[0].split(":")[1]
    return p

class Solver:
    def solve_capmonster(site_key, page_url):
        config = json.loads(open('config.json', 'r').read())
        key = config["captcha_keys"]["capmonster"]
        url = "https://api.capmonster.cloud/createTask"
        data = {
            "clientKey": key,
            "task":
            {
                "type": "HCaptchaTaskProxyless",
                "websiteURL": page_url,
                "websiteKey": site_key
            }
        }
        response = httpx.post(url,json=data)
        if response.json()['errorId'] == 0:
            task_id = response.json()['taskId']
            url = "https://api.capmonster.cloud/getTaskResult"
            data = {
                "clientKey": key,
                "taskId": task_id
            }
            response = httpx.post(url,json=data)
            while response.json()['status'] == 'processing':
                time.sleep(3)
                response = httpx.post(url,json=data)
            return response.json()['solution']['gRecaptchaResponse']
        else:
            return False
        
class Solver2:
    config = json.loads(open('config.json', 'r').read())
    key = config['captcha_keys']['capsolver']
    def __init__(self, proxy:str, siteKey:str, siteUrl:str) -> None:
        self.debug = False
        self.proxy = proxy

        self.siteKey = siteKey
        self.siteUrl = siteUrl

    def log(self, txt:str) -> None:
        if self.debug: print(txt)

    def solveCaptcha(self) -> str:
        r = requests.post(f"https://api.capsolver.com/createTask",json=payload("capsolver.com",self.proxy,'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'))
        try:
            if r.json().get("taskId"):
                taskid = r.json()["taskId"]
            else:
                return None
        except:
            return None

        while True:
            try:
                r = requests.post(f"https://api.capsolver.com/getTaskResult",json={"clientKey":key,"taskId":taskid})
                if r.json()["status"] == "ready":
                    key = r.json()["solution"]["gRecaptchaResponse"]
                    return key
                elif r.json()['status'] == "failed":
                    return None
            except:
                return None