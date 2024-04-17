from openai import OpenAI
import streamlit as st
from googlesearch import search
from utility_search_corporate_or_news import is_corp
from utility_generate_search_query import search_query_gen
from googlesearch import search

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
selected_model = "gpt-3.5-turbo"

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States.'
user_input = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States from the their companies web.'

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
        # print(len(aaa))

        for idx, result in enumerate(aaa, 1):
            print(f"{idx}. {result}")


