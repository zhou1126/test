import streamlit as st
api_key=st.secrets["OPENAI_API_KEY"]
print(api_key)

from openai import OpenAI
client = OpenAI(api_key=api_key)

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

completion = client.chat.completions.create(
  model= "gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": '''You are a Google engineer and you will receive user's input. Find what the user trying to search for. Just answer the object/subject what the user want to find out.'''},
    {"role": "user", "content": "I want to know Tesla (TSLA) news"}
  ],
  temperature=0.0,
  top_p=0.95,  
)
print(completion.choices[0].message.content)