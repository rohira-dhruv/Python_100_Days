import pandas
import datetime as dt
import random
import smtplib
PLACEHOLDER = "[NAME]"
MY_EMAIL = "gl1tch.djr@gmail.com"
MY_PASSWORD = "yhdyslduogyvrxxs"

data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()

for (index, row) in data.iterrows():
    if row.month == today.month and row.day == today.day:

        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as mail_template_file:
            mail_template = mail_template_file.read()
        mail_to_send = mail_template.replace(PLACEHOLDER, f"{row['name']}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{row.email}",
                msg=f"Subject:Happy Birthday!\n\n{mail_to_send}"
            )
