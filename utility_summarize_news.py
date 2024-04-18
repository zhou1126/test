import requests
from bs4 import BeautifulSoup
from datetime import datetime

def new_summary(client_def, link, selected_model, temperature, top_p, start_time, end_time):
    news_response = requests.get(link)
    # Create a BeautifulSoup object to parse the news page content
    news_soup = BeautifulSoup(news_response.content, 'html.parser')
    print(news_soup)

    # Find the publish time element
    publish_time_element = news_soup.find('time')
    # publish_time_element = news_soup.find_all("time")
    print(publish_time_element)

    determine_time = client_def.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": f'''You are a HTML developer. Find the publish time. If the publish time is between {start_time} and {end_time} output 1, otherwise output 0.'''},
                        {"role": 'user', "content": str(publish_time_element)}]
                    ,
                    temperature=temperature,
                    top_p=top_p,
                    # stream=True,
            )
    print(determine_time.choices[0].message.content)

    if determine_time.choices[0].message.content == '1':
        article_text  = news_soup.find().get_text(strip=True)
        print(article_text)

        article_sum = client_def.chat.completions.create(
                    model=selected_model,
                    messages=[
                        {"role": "system", "content": '''You are a HTML developer. Read the following codes, find the main content and summarize it. Only output the summary'''},
                        {"role": 'user', "content": str(article_text)}]
                    ,
                    temperature=temperature,
                    top_p=top_p,
                    # stream=True,
            )
        print(article_sum.choices[0].message.content)

        return article_sum.choices[0].message.content