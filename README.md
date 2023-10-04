# ProxyUNI
**Infinite proxy program has HTTP&HTTPS 1597 proxies**

This program receives its proxies from the `proxyscrape.com` service, and using some rules, we put these proxies together in an orderly manner so that you can access them more easily.

# Rules

```Python
ange_i = int(input('How many proxies do you want?(limit 2057) '))
if range_i <= end:
    for genrate in range(range_i):
        response = requests.post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx', json=data)
        proxies = response.text.split('\n')

        proxy = proxies[start]
        print(C.BLUE, proxy)
        start += 1
        counter += 1

        if counter == range_i:
            print(C.YELLOW+'Proxy termination')
            break
```
Also, this program uses the `httpdebugger.com` service, because of the `proxyscrape.com` filter, we pass requests through this service so that we can reject the filter.
