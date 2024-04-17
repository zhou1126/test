from openai import OpenAI
import streamlit as st
from googlesearch import search

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# selected_model = "gpt-3.5-turbo"

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# prompt = 'Search 2024 News and updates from the following companies for the United States, Brother, Panduit, Dymo, Epson, Phoenix Contact, King Jim, Zebra, TSC, CAB, SATO, Honeywell, Bixolon, Duralabel, Labeltac, Tradesafe, Masterlock, Abus, Justrite, AccuformNMC, Mighty Line, Brimar Industries, WW Grainger, Uline, Vallen, New Pig, ChemTex, SpillTech, FyterTech, MBT, Almetek, Uticom, William Frick, LEM Products, Trident Company, Fastenal Company, Graybar Electric Co, RS Hughes Co, Heilind Electric, Consolidated Electrical, MSC Industrial Supply, Wesco Distribution Inc.'

def search_query_gen(client_def, prompt, selected_model, temperature, top_p):
    search_for = client_def.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": "system", "content": '''You are a Google engineer and will receive a prompt with a list of company names. Find the corresponding search query on Google per company. Show me the search query in bullet points and separated by "\n".'''},
                            {"role": 'user', "content": prompt}]
                        ,
                        temperature=temperature,
                        top_p=top_p,
                        # stream=True,
                )
    # print(search_for.choices[0].message.content)
    return search_for.choices[0].message.content

# user_input = 'Here is a list of companies: Brother, Panduit. Search 2024 News and updates for the United States from the their companies web.'
# search_query_list = search_query_gen(client, user_input, selected_model, 0, 0.95)
# print(search_query_list)