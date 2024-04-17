from openai import OpenAI
import streamlit as st
from googlesearch import search

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# selected_model = "gpt-3.5-turbo"

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

def is_corp(client_def, prompt, selected_model, temperature, top_p):
    is_corporate = client_def.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a Google engineer and will receive a search prompt. Tell me whether the user want to search on the corporate webpage or general News. Return True if user wants to search on Corporate Web, return False if user wants to search on general news.'''},
                        {"role": 'user', "content": prompt}]
                    ,
                    temperature=temperature,
                    top_p=top_p,
                    # stream=True,
            )
    # print(is_corporate.choices[0].message.content)
    return is_corporate.choices[0].message.content

# prompt = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States from the their companies web.'
# prompt = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States.'

# is_corp_yes = is_corp(client, prompt, "gpt-3.5-turbo", 0, 0.95)
# print(f"{prompt} is search on corp? {is_corp_yes}")