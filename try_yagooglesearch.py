import yagooglesearch
# from utility_proxy import get_proxies 
# from itertools import cycle

# proxies_list = get_proxies()
# print(proxies_list)
# proxy_pool = cycle(proxies_list)

query = 'Brother company news updates United States 2024'

# for i in range(1,11):
#     proxy = next(proxy_pool)

client = yagooglesearch.SearchClient(
    query,
    # tbs="li:1",
    num=3,
    # max_search_result_urls_to_return=100,
    http_429_cool_off_time_in_minutes=45,
    http_429_cool_off_factor=1.5,
    # proxy= proxy,
    # verbosity=5,
    # verbose_output=True,  # False (only URLs) or True (rank, title, description, and URL)
)
client.assign_random_user_agent()

urls = client.search()

len(urls)

for url in urls:
    print(url)