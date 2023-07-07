import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "QYMB6GNYNJ9X8Z2K"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_API_KEY = "e3a83cbd298c4f56bca6855b13df224f"
NEW_API_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_AUTH_TOKEN = "1389aae6144ebd193d520e1a1ab527ce"
TWILIO_ACCOUNT_SID = "ACf82b29f3718ba711a9e53f9e7bb836ca"
TWILIO_PHONE = "+18145264325"


stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
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

if percent_diff > 1:
    news_response = requests.get(url=NEW_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    article_list = news_response.json()["articles"][0:3]
    if is_up:
        arrow_emoji = "🔺"
    else:
        arrow_emoji = "🔻"
    formatted_articles = [f"{STOCK}: {arrow_emoji}{round(percent_diff)}% \nHeadline: {article['title']}. \nBrief: "
                          f"{article['description']}" for article in article_list]
    client = Client(username=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        client.messages.create(
            from_=TWILIO_PHONE,
            to="+916386932267",
            body=article
        )
