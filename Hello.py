# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import streamlit as st
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)




# def run():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )

#     st.write("# Welcome to Streamlit! ")

#     st.sidebar.success("Select a demo above.")

#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.
#         **👈 Select a demo from the sidebar** to see some examples
#         of what Streamlit can do!
#         ### Want to learn more?
#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)
#         ### See more complex demos
#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )


# if __name__ == "__main__":
#     run()

from openai import OpenAI
import streamlit as st
from gnews import GNews

def search(google_sql, period_parameter = '24h', top_n = 3):
    google_news = GNews(language='en', country='US', period=period_parameter)
    # google_sql = 'Data Center construction projects ' + 'United States'
    # google_sql = 'Hospital construction projects ' + 'United States'

    json_resp = google_news.get_news(google_sql)
    
    if len(json_resp) > 0:
        return json_resp[:top_n]
    else:
        return "No news found"
    
def news_content(url, period_parameter = '24h'):
    google_news = GNews(language='en', country='US', period=period_parameter)
    article = google_news.get_full_article(url) 
    return article
    
topn = 3
time_frame = '60d'
openai_api_key = "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"
selected_model = "gpt-3.5-turbo"

# json_resp = search('Tesla(TSLA) news', period_parameter = time_frame, top_n = topn)
# print(json_resp)

st.title("News Aggregator Sandbox")

# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
client = OpenAI(api_key=openai_api_key)

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        search_for = client.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a Google engineer and you will receive user's input. Find what the user trying to search for. Just answer the object/subject what the user want to find out.'''},
                        {"role": 'user', "content": prompt}]
                    ,
                    # messages=[
                    #     [{"role":"system","content":'''You are a Google engineer and you will receive user's input. Find what the user trying to search for. Just answer the object/subject what the user want to find out.'''}, {"role": m["role"], "content": m["content"]}]
                    #     for m in st.session_state.messages
                    # ],
                    temperature=0.0,
                    top_p=0.95,
                    # stream=True,
            )
        # print(search_for.choices[0].message.content)
        # response = st.write_stream(search_for)

        json_resp = search(search_for.choices[0].message.content, period_parameter = time_frame, top_n = topn)
        # print(json_resp)

        for i in range(len(json_resp)):
            # try: 
            article = news_content(json_resp[i]['url'])
            # print(article.title)
            prompt = f'[USER]: The title of the article is: "{article.title}"' + '\n'
            prompt += f'Summarize the content in one paragraph.' + '\n'
            prompt += article.text
            # print(prompt)
            # response = st.write_stream(article.title)
            completion = client.chat.completions.create(
                        model= selected_model,
                        messages=[
                            {"role": "system", "content": '''You are an analyst specializing summarizing news.'''},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.0,
                        top_p=0.95,  
                        stream=True,
                        )
            response = st.write_stream(completion)
            st.write(article.title)
            st.write(json_resp[i]['url'])

                # print(completion.choices[0].message.content)
            # except:
            #     print('link does not work.') 

    # with st.chat_message("assistant"):
    #     stream = client.chat.completions.create(
    #         model=st.session_state["openai_model"],
    #         messages=[
    #             {"role": m["role"], "content": m["content"]}
    #             for m in st.session_state.messages
    #         ],
    #         stream=True,
    #     )
    #     response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

