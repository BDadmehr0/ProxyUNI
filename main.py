import requests
import os
from colorama import Fore as C

end = 2057
start = 366
url = 'https://api.ipify.org?format=json'
    
counter = 0 
data = {
    'UrlBox': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
    'AgentList': 'Internet+Explorer',
    'VersionsList': 'HTTP%2F1.1',
    'MethodList': 'GET',
}

def Banner():
    print('  ___                  _   _ _  _ ___  ')
    print(' | _ \_ _ _____ ___  _| | | | \| |_ _| '+C.CYAN+'help: 00',C.WHITE)
    print(" |  _/ '_/ _ \ \ / || | |_| | .` || |  "+C.CYAN+'Github BDadmehr0',C.WHITE)
    print(' |_| |_| \___/_\_\\_,  |\___/|_|\_|___| '+C.CYAN+'Infinite proxy program has 1597 proxies',C.WHITE)
    print('                  |__/                 V1.0.0\n',C.WHITE)

def help():
    print(C.CYAN+'\ncommand      about\n')
    print('10           Start')
    print('11           Show Your public IP')
    print('12           Clear Terminal')
    print('13           Quit\n',C.WHITE)


if __name__ == "__main__":
    Banner()
    while True:
        qus_i = int(input('ProxyUNI-Command$: '))
        if qus_i == 10:
            range_i = int(input('How many proxies do you want?(limit 2057) '))
            if range_i <= end:
                for genrate in range(range_i):
                    try:
                        response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', json=data)
                        proxies = response.text.split('\n')
        
                        proxy = proxies[start]
                        print(counter, C.BLUE, proxy,C.WHITE)
                        start += 1
                        counter += 1
        
                        if counter == range_i: 
                            break
                    except requests.exceptions.ConnectionError:
                        print(C.YELLOW+'requests.exceptions.ConnectionError: Check Your intetnet an try again',C.WHITE)
            else:
                print(c.RED+'Not available this many Proxy',C.WHITE)
        elif qus_i == 00:
            help()
        elif qus_i == 11:
            try:
                response = requests.get(url)
                data = response.json()

                ip_address = data['ip']
                print(ip_address)
            except requests.exceptions.ConnectionError:
                print(C.YELLOW+'requests.exceptions.ConnectionError: Check Your intetnet an try again',C.WHITE)
        elif qus_i == 12:
            os.system('clear')
        elif qus_i == 13:
            exit()
        else:
            print(C.RED+'Terminal: Command not available',C.WHITE)
