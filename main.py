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
    print('command      about')
    print('11           Show Your public IP')
    print('12           Clear Terminal')
    print('13           Quit')


if __name__ == "__main__":
    Banner()
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
                print('requests.exceptions.ConnectionError: Check Your intetnet an try again')
    elif rage_i == 00:
        help()
    elif range_i == 11:
        response = requests.get(url)
        data = response.json()

        ip_address = data['ip']
        print(ip_address)
    elif range_i == 12:
        os.system('clear')
    elif range_i == 13:
        exit()
    else:
        print(C.RED+'Proxy Limit(2057): This amount of proxy is not available')
