from openai import OpenAI
import streamlit as st
from googlesearch import search
from utility_search_corporate_or_news import is_corp
from utility_generate_search_query import search_query_gen
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from utility_determine_navigation import is_navigation_page
import os
from difflib import SequenceMatcher

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
selected_model = "gpt-3.5-turbo"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# user_input = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States.'
user_input = 'Here is a list of companies: Brother. Search 2024 News and updates for the United States from the their companies web.'

# Check whether it is searching on Corporate Web or general News
is_corp_yes = is_corp(client, user_input, selected_model, 0, 0.95)
print(f"{user_input} is search on corp? {is_corp_yes}")

if is_corp_yes == "True":
    search_query_list = search_query_gen(client, user_input, selected_model, 0, 0.95)
    print(search_query_list)

    search_list_separated = search_query_list.split("\n")
    print(len(search_list_separated))

    for search_q in search_list_separated:
        search_q = search_q.replace('- ', '')
        search_q = search_q.replace('.com', '')
        print(search_q)

        # grab the weblinks
        aaa = search(f"{search_q}", lang="en",  sleep_interval=2, num_results=1)
        # print(aaa)
        for base_url in aaa:
            print(base_url)

            response = requests.get(base_url)
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all the <a> tags with "href" attribute
            links = soup.find_all('a', href=True)
            print(links)
            # Extract the news links
            news_links = []
            for link in links:
                href = link['href']
                print(href)

                matcher = SequenceMatcher(None, base_url, href)
                match = matcher.find_longest_match(0, len(base_url), 0, len(href))

                # Combine the URLs
                combined_url = base_url + '/' + href[match.size:]
                combined_url =combined_url.replace("//", "/")
                news_links.append(combined_url)

            print(news_links)
            # Iterate over each news link
            for link in news_links[:]:

                nevigation_yes = is_navigation_page(link)
                print(f"{link} nevigation? {nevigation_yes}") 
                    # for idx, result in enumerate(aaa, 1):
                    #     print(f"{idx}. {result}")


