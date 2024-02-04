import os
import random

import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "0JD3UHM3U5WSJU6LK"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = "e3a83cbd298c4f56bca6855b13df224f"
NEW_API_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SSID")
TWILIO_PHONE = "+16592347418"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "apikey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title",
}

response = requests.get(url=STOCK_API_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = float(stock_data_list[0]["4. close"])
prev_closing_price = float(stock_data_list[1]["4. close"])
is_up = yesterday_closing_price > prev_closing_price
change = abs(yesterday_closing_price - prev_closing_price)
percent_diff = change/prev_closing_price*100

if percent_diff > 0.5:
    news_response = requests.get(url=NEW_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    article_list = news_response.json()["articles"][0:3]
    if is_up:
        arrow_emoji = "up"
    else:
        arrow_emoji = "down"
    formatted_articles = [f"{STOCK}: {round(percent_diff, 2)}% {arrow_emoji}\nHeadline: {article['title']}. \nBrief: "
                          f"{article['description']}" for article in article_list]
    client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    article = random.choice(formatted_articles)
    client.messages.create(
        from_=TWILIO_PHONE,
        to="+916386932267",
        body=article
    )
