import os
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.043490 # Your latitude
MY_LONG = 31.235290 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# Credentials are read from environment variables (see .env.example) instead of being hard-coded.
my_email = os.environ.get("SENDER_EMAIL")
password = os.environ.get("SENDER_PASSWORD")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_latitude in range(25,35) and iss_longitude in range(25,35):
        if sunset <= time_now.hour <= sunrise:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(my_email,password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=os.environ.get("RECIPIENT_EMAIL"),
                                    msg=f"Subject:LOOK OUT!\n\n THE ISS IS OVER YOUR HEAD!")


