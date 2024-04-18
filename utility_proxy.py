import requests
from lxml.html import fromstring
from itertools import cycle


def get_proxies():
    # Method to scrape a list of free proxy IP addresses for aid in webscraping Amazon pages
    # returns: 
    #         - Set, a list of the current available proxies, updated on the website every 10 minutes (1/1/2023)
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

proxies_list = get_proxies()
print(proxies_list)

proxy_pool = cycle(proxies_list)
print(proxy_pool)

for i in range(1,11):
    proxy = next(proxy_pool)
    print(proxy)
