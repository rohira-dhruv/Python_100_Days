import datetime as dt
import smtplib
import random

MY_EMAIL = "jacobperalta00000@gmail.com"
MY_PASSWORD = "govijejqohkapwxt"

now = dt.datetime.now()
weekday = now.weekday()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    if weekday == 0:
        with open("quotes.txt") as data_file:
            quote_list = data_file.readlines()
        random_quote = random.choice(quote_list)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )
