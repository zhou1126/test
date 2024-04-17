import requests
from bs4 import BeautifulSoup

def is_navigation_page(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Check if the page contains a high number of internal links
    internal_links = soup.find_all('a', href=lambda href: href and href.startswith('/') and href.endswith('html'))
    print(internal_links)
    print(len(internal_links))
    
    # Check if the page has a low amount of content (e.g., text)
    content = soup.get_text()
    print(len(content))
    
    # Define a threshold for the number of internal links and content length
    link_threshold = 10
    content_threshold = 500
    
    # Determine if the page is a navigation page based on the thresholds
    if len(internal_links) >= link_threshold or len(content) < content_threshold:
        return True
    else:
        return False

# Example usage
url1 = "https://www.kingjim.co.jp/english/news/year-2024"
url2 = "https://www.kingjim.co.jp/english/news/detail/127.html"

url_list = ['https://www.kingjim.co.jp/english/news/detail/127.html', 'https://www.kingjim.co.jp/english/news/detail/126.html', 'https://www.kingjim.co.jp/english/news/detail/129.html', 'https://www.kingjim.co.jp/english/news/detail/128.html', 'https://www.kingjim.co.jp/english/news/detail/122.html', 'https://www.kingjim.co.jp/english/news/detail/120.html', 'https://www.kingjim.co.jp/english/news/detail/119.html', 'https://www.kingjim.co.jp/english/news/detail/117.html', 'https://www.kingjim.co.jp/english/news/detail/118.html', 'https://www.kingjim.co.jp/english/news/year-2023', 'https://www.kingjim.co.jp/english/news/year-2022', 'https://www.kingjim.co.jp/english/news/year-2021', 'https://www.kingjim.co.jp/english/news/year-2020', 'https://www.kingjim.co.jp/english/news/year-2019', 'https://www.kingjim.co.jp/english/news/year-2018']
# url_list = ['https://www.kingjim.co.jp/english/news/year-2018']

for url in url_list:
    nevigation_yes = is_navigation_page(url)
    print(f"{url} nevigation? {nevigation_yes}")  # Output: True
# print(is_navigation_page(url2))  # Output: False