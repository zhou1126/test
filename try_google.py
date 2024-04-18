import requests
from bs4 import BeautifulSoup


googleTrendsUrl = 'https://google.com'
response = requests.get(googleTrendsUrl)
if response.status_code == 200:
    g_cookies = response.cookies.get_dict()
    # print(g_cookies)


input_str = '- "Brother company news updates United States 2024"'
# Remove leading and trailing characters ("- " and """)
cleaned_str = input_str.strip('- "').strip('"')
# Replace spaces with '+'
modified_str = cleaned_str.replace(" ", "+")

# query = 'selenium'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
url = 'https://www.google.com?q=' + modified_str
res = requests.get(url, headers=headers, cookies=g_cookies)
print(res)

if res.status_code == 200: #if the endpoint answers
    # state = res.content.decode("utf-8")
    # print(res.content)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup)

    with open('search_results.txt', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    search_results = soup.find_all('div', class_='tF2Cxc')
    # print(search_results)
    for result in search_results:
        link = result.find('a')['href']
        print(link)
    # print(state)

# import requests

# googleTrendsUrl = 'https://google.com'
# response = requests.get(googleTrendsUrl)
# if response.status_code == 200:
#     g_cookies = response.cookies.get_dict()

# input_str = '- "Brother company news updates United States 2024"'
# cleaned_str = input_str.strip('- "').strip('"')
# modified_str = cleaned_str.replace(" ", "+")

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
#             AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
# url = 'https://www.google.com/search?q=' + modified_str
# res = requests.get(url, headers=headers, cookies=g_cookies)
# print(res)

# if res.status_code == 200:
#     soup = BeautifulSoup(res.content, 'html.parser')
#     search_results = soup.find_all('div', class_='yuRUbf')
    
#     for result in search_results:
#         link = result.find('a')['href']
#         print(link)