# import smtplib

# my_email = os.environ.get("SENDER_EMAIL")
# password = os.environ.get("SENDER_PASSWORD")

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)

#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="recipient@example.com",
#         msg="Subject:Hello\n\nThis is the body"
#     )


import os
import datetime as dt
import smtplib
import random


# Credentials are read from environment variables (see .env.example) instead of being hard-coded.
my_email = os.environ.get("SENDER_EMAIL")
password = os.environ.get("SENDER_PASSWORD")


now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
date_of_birth = dt.datetime(year=2004, month=3, day=20, hour=2)


with open("quotes.txt") as file:
    data = file.readlines()
    
if weekday == 5:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.environ.get("RECIPIENT_EMAIL"),
            msg=f"Subject:Your Quote\n\n{random.choice(data)}"
        )





