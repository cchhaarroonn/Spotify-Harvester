import os, requests, ctypes, random, string, threading
from colorama import Fore
from fake_useragent import UserAgent

ua = UserAgent()

green = Fore.GREEN
reset = Fore.RESET

ctypes.windll.kernel32.SetConsoleTitleW(f"Spotify Harvester")
generated = 0
errors = 0
proxyList = []

if os.name == "NT":
    os.system("cls");
else:
    os.system("clear");

print(f"""{green}
   _____             _   _  __         _    _                           _            
  / ____|           | | (_)/ _|       | |  | |                         | |           
 | (___  _ __   ___ | |_ _| |_ _   _  | |__| | __ _ _ ____   _____  ___| |_ ___ _ __ 
  \___ \| '_ \ / _ \| __| |  _| | | | |  __  |/ _` | '__\ \ / / _ \/ __| __/ _ \ '__|
  ____) | |_) | (_) | |_| | | | |_| | | |  | | (_| | |   \ V /  __/\__ \ ||  __/ |   
 |_____/| .__/ \___/ \__|_|_|  \__, | |_|  |_|\__,_|_|    \_/ \___||___/\__\___|_|   
        | |                     __/ |                                                
        |_|                    |___/                                                 

                        Proudly made by charon with <3
{reset}""")

print(f"{green}Loading proxies...{reset}")

with open ("proxies.txt","r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        proxyList.append(line)
    if len(proxyList) == 0:
        print(f"{reset}Proxies file is empty, please put in proxies."); quit()

print(f"{green}Loaded proxies, starting to generate ...{reset}")

def create():
    try:
        email = ("").join(random.choices(string.ascii_letters + string.digits, k=6)) + "@charon.gay"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k=9))
        username  = ("CharonGay").join(random.choices(string.ascii_letters + string.digits, k=5))

        proxies = { 
        "http": f"http://{proxyList[i]}", 
        "https": f"http://{proxyList[i]}", 
        "ftp": f"ftp://{proxyList[i]}"}

        headers = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 5.2; en-US; rv:1.9.0.20) Gecko/20150911 Firefox/36.0",
            "Referer": "https://www.spotify.com/",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*"
        }

        url = "https://spclient.wg.spotify.com/signup/public/v1/account"
        data = f"&birth_day=2&birth_month=02&birth_year=1990&collect_personal_info=undefined&creation_flow=&creation_point=https%3A%2F%2Fwww.spotify.com%2Fnl%2F&displayname={username}&gender=male&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&platform=www&referrer=&send-email=1&thirdpartyemail=1&email={email}&password={password}&password_repeat={password}"
        r = requests.post(url,headers=headers,data=data,proxies=proxies)

        if '{"status":1,' in r.text:
            with open(f"generated.txt", "a") as f:
                f.write(f"{email}:{password}\n")
                generated += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Spotify Harvester - Generated: {generated} | Errors: {errors}")
        elif '{"status":320,"errors":' in r.text:
            errors += 1
        elif '{"status":0,"errors":{"attempts":}' in r.text:
            errors += 1
        elif '504' in r.text:
            errors += 1
        elif 'The server encountered a temporary error and could not complete your request' in r.text:
            errors += 1
        else:
            errors += 1
            pass
    except Exception as e: 
        pass

for i in range(len(proxyList)):
    try:
        threading.Thread(target=create).start()
        threading.Thread(target=create).start()
        threading.Thread(target=create).start()
    except Exception as e:
        pass

