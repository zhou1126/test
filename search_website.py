from openai import OpenAI
import streamlit as st
from googlesearch_customized import search

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
selected_model = "gpt-3.5-turbo"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = 'Search 2024 News and updates from the following companies for the United States, Brother, Panduit, Dymo, Epson, Phoenix Contact, King Jim, Zebra, TSC, CAB, SATO, Honeywell, Bixolon, Duralabel, Labeltac, Tradesafe, Masterlock, Abus, Justrite, AccuformNMC, Mighty Line, Brimar Industries, WW Grainger, Uline, Vallen, New Pig, ChemTex, SpillTech, FyterTech, MBT, Almetek, Uticom, William Frick, LEM Products, Trident Company, Fastenal Company, Graybar Electric Co, RS Hughes Co, Heilind Electric, Consolidated Electrical, MSC Industrial Supply, Wesco Distribution Inc.'

search_for = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a Google engineer and will receive a list of companies. Find the corresponding search query per company by bullet points. And just show the bullet points.'''},
                        {"role": 'user', "content": prompt}]
                    ,
                    temperature=0.0,
                    top_p=0.95,
                    # stream=True,
            )
print(search_for.choices[0].message.content)

search_for_item = 'King Jim company updates 2024 US'
# aaa = search(f"{search_for_item}", lang="en",  sleep_interval=1, num_results=1)
aaa = search(f"{search_for_item}", lang="en",  sleep_interval=1, num_results=1)
# print(len(aaa))

for idx, result in enumerate(aaa, 1):
    print(f"{idx}. {result}")

import requests
from bs4 import BeautifulSoup
from datetime import datetime

base_url = 'https://www.kingjim.co.jp/english/news/year-2024'
# Send a GET request to the webpage
response = requests.get(base_url)
# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Find all the <a> tags with "href" attribute
links = soup.find_all('a', href=True)
# Extract the news links
news_links = []
for link in links:
    href = link['href']
    if href.startswith('/english/news/') and href != '/english/news/year-2024':
        news_links.append('https://www.kingjim.co.jp' + href)

print(news_links)
# Iterate over each news link
for link in news_links[:1]:
    # Send a GET request to the news page
    news_response = requests.get(link)
    # Create a BeautifulSoup object to parse the news page content
    news_soup = BeautifulSoup(news_response.content, 'html.parser')
    print(news_soup)

    # Find the publish time element
    publish_time_element = news_soup.find('time')
    # publish_time_element = news_soup.find_all("time")
    print(publish_time_element)

    determine_time = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a HTML developer. Find the publish time. If the publish time is between 2024-03-01 and 2024-04-16 output 1, otherwise output 0.'''},
                        {"role": 'user', "content": str(publish_time_element)}]
                    ,
                    temperature=0.0,
                    top_p=0.95,
                    # stream=True,
            )
    print(determine_time.choices[0].message.content)

    if determine_time.choices[0].message.content == '1':
        article_text  = news_soup.find().get_text(strip=True)
        print(article_text)

        article_sum = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a HTML developer. Read the following codes, find the main content and summarize it. Only output the summary'''},
                        {"role": 'user', "content": str(article_text)}]
                    ,
                    temperature=0.0,
                    top_p=0.95,
                    # stream=True,
            )
        print(article_sum.choices[0].message.content)