import os, json, time, random, string, ctypes, getpass, sys, threading, concurrent.futures, base64

try:
    import tls_client
    import colorama
    import httpx
    import datetime
    import pystyle
    import requests
    import websocket
except ModuleNotFoundError:
    os.system("pip install tls_client")
    os.system("pip install colorama")
    os.system("pip install httpx")
    os.system("pip install datetime")
    os.system("pip install pystyle")
    os.system("pip install requests")
    os.system("pip install websocket")

from tls_client import Session
from colorama import Fore, Style
from pystyle import Write, System, Colors, Colorate
from datetime import datetime
from modules.solvers import Solver, Solver2
from websocket import WebSocket

output_lock = threading.Lock()
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT

generated = 0
solved = 0
errors = 0
total = 0

ctypes.windll.kernel32.SetConsoleTitleW(f"[ Feed Gen ] By H4cK3dR4Du & PyController | github.com/H4cK3dR4Du ~ github.com/PyController")
class Utils:
    @staticmethod
    def generate_mail():
        config = json.loads(open('config.json', 'r').read())
        mail_domain = config["custom_settings"]["mail_domain"]
        if mail_domain == "" or mail_domain is None:
            email = f"tls_spoofing{random.randint(0, 10000000)}@radupycontroller{random.randint(0, 99999999)}.com"
            return email
        else:
            email = f"{mail_domain}{random.randint(0, 10000000)}@{mail_domain}{random.randint(0, 99999999)}.com"
            return email

    @staticmethod
    def generate_password():
        config = json.loads(open('config.json', 'r').read())
        password = config["custom_settings"]["password"]
        if password == "":
            password = f"tls_spoofing{random.randint(0, 10000000)}"
            return password
        else:
            password = f"{password}{random.randint(0, 10000000)}"
            return password

    @staticmethod
    def get_fingerprint(session):
        resp = session.get("https://discord.com/api/v9/experiments")
        json_response = resp.json()
        fingerprint = json_response['fingerprint']
        return fingerprint, resp.cookies

    @staticmethod
    def get_time():
        date = datetime.now()
        hour, minute, second = date.hour, date.minute, date.second
        timer = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
        return timer

    @staticmethod
    def get_username():
        config = json.loads(open('config.json', 'r').read())
        username = config["custom_settings"]["username"]
        if username == None or username == "":
            url = "https://raw.githubusercontent.com/TahaGorme/100k-usernames/main/usernames.txt"
            response = requests.get(url)
            names = response.text.splitlines()
            username = random.choice(names)
            return username
        else:
            username = "tls_spoofing"
            return username

    @staticmethod
    def get_birthdate():
        birthdate = f'{random.randint(1980, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}'
        return birthdate
    
    @staticmethod
    def online_token(token):
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')        
        try:
            ws_online = websocket.WebSocket()
            ws_online.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            platform = sys.platform
            details = "github.com/H4cK3dR4Du\ngithub.com/PyController"
            state = "Made By Radu & PyController"
            name = "tls_spoofing"
            status_list = ["online", "idle", "dnd"]
            status = random.choice(status_list)
            ws_online.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": platform,
                        "$browser": "RTB",
                        "$device": f"{platform} Device",
                    },
                    "presence": {
                        "game": {
                            "name": name,
                            "type": 0,
                            "details": details,
                            "state": state,
                        },
                    "status": status,
                    "since": 0,
                    "activities": [],
                    "afk": False,
                },
            },
            "s": None,
            "t": None
            }))
        except:
            pass

    @staticmethod
    def get_invite():
        config = json.loads(open('config.json', 'r').read())
        invite = config["custom_settings"]["invite_code"]
        if invite == "" or invite is None:
            invite_code = None
            return invite_code
        else:
            return invite
        
    @staticmethod
    def get_xsup():
        prop = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "es-ES",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "browser_version": "113.0.0.0",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 218604,
            "client_event_source": None
        }

        xsuper = base64.b64encode(json.dumps(prop, separators=(',', ':')).encode()).decode()
        return xsuper
    
    
def member_booster():
    global generated, solved, errors, total
    chrome_version = 112

    with open("proxies.txt") as proxies:
        proxy_lines = proxies.readlines()
        proxy = random.choice(proxy_lines).strip()
    
    session = tls_client.Session(
        client_identifier=f"chrome_112",
        random_tls_extension_order=True
    )
    
    session.proxies = {
        "http": "http://" + proxy,
        "https": "https://" + proxy
    }

    email = Utils.generate_mail()
    password = Utils.generate_password()
    username = Utils.get_username()
    fingerprint, xxxcookies = Utils.get_fingerprint(session)
    birthday = Utils.get_birthdate()
    invite_code = Utils.get_invite()
    xsuper = Utils.get_xsup()

    config = json.loads(open('config.json', 'r').read())
    capsolver_key = config["captcha_keys"]["capsolver"]
    capmonster_key = config["captcha_keys"]["capmonster"]

    if capsolver_key is None or capsolver_key == "":
        key = Solver.solve_capmonster(f"4c672d35-0701-42b2-88c3-78380b0db560", "https://discord.com/")
    else:
        solver = Solver2(proxy=proxy, siteKey="4c672d35-0701-42b2-88c3-78380b0db560", siteUrl="discord.com")
        key = solver.solveCaptcha()

    time_rn = Utils.get_time()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({cyan}*{gray}) {pretty}Solved {gray}| {pink}{key[:60]}*********")

    cookies = {
        '__dcfduid': xxxcookies.get('__dcfduid'),
        '__sdcfduid': xxxcookies.get('__sdcfduid'),
        '__cfruid': xxxcookies.get('__cfruid'),
        'locale': 'es-ES',
    }

    payload = {
        "consent": True,
        "fingerprint": fingerprint,
        "username": username,
        "captcha_key": key,
        "invite": invite_code
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.9',
        'Connection': 'keep-alive',
        'content-length': str(len(json.dumps(payload))),
        'Content-Type': 'application/json',
        'Origin': 'https://discord.com',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Fingerprint': fingerprint,
        'X-Track': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
    }

    response = session.post(f"https://discord.com/api/v9/auth/register", headers=headers, cookies=cookies ,json=payload)
    token = response.json()['token']
    time_rn = Utils.get_time()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Generated {gray}| {dark_green}{token}")
    Utils.online_token(token)
    with open("tokens.txt", "a") as file:
        file.write(token + "\n")
    member_booster()

config = json.loads(open('config.json', 'r').read())
threads = []
howmany = config["custom_settings"]["threads"]

for _ in range(int(howmany)):
    thread = threading.Thread(target=member_booster)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()