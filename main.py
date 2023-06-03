import requests
import os
from colorama import Fore as C
os.system('clear')

end = 2057
start = 366

counter = 0  # متغیر شمارنده
data = {
    'UrlBox': 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
    'AgentList': 'Internet+Explorer',
    'VersionsList': 'HTTP%2F1.1',
    'MethodList': 'GET',
}

def Banner():
    print('  ___                  _   _ _  _ ___  ')
    print(' | _ \_ _ _____ ___  _| | | | \| |_ _| ')
    print(" |  _/ '_/ _ \ \ / || | |_| | .` || |  "+C.CYAN+'Github BDadmehr0',C.WHITE)
    print(' |_| |_| \___/_\_\\_, |\___/|_|\_|___| '+C.CYAN+'Infinite proxy program has 1597 proxies',C.WHITE)
    print('                  |__/                 V1.0.0\n',C.WHITE)

if __name__ == "__main__":
    Banner()
    range_i = int(input('How many proxies do you want?(limit 2057) '))
    if range_i <= end:
        for genrate in range(range_i):
            response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', json=data)
            proxies = response.text.split('\n')

            proxy = proxies[start]  # یک پروکسی را انتخاب کنید
            print(C.BLUE, proxy)
            start += 1
            counter += 1  # افزایش شمارنده

            if counter == range_i:  # بررسی اگر شمارنده برابر با تعداد مورد نظر بشود
                print(C.YELLOW+'Proxy termination')
                break 

    else:
        print(C.RED+'Proxy Limit(2057): This amount of proxy is not available')
