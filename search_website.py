from openai import OpenAI
import streamlit as st
from googlesearch import search

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
aaa = search(f"{search_for_item}", lang="en",  num_results=1)
# print(len(aaa))

for idx, result in enumerate(aaa, 1):
    print(f"{idx}. {result}")