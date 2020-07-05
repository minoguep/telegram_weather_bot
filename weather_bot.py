import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# send request to API for forecast
url = f"https://api.openweathermap.org/data/2.5/forecast?id={os.environ['OPEN_WEATHER_LOCATION']}&" \
      f"APPID={os.environ['OPEN_WEATHER_TOKEN']}&mode=json&units=metric"

data = requests.get(url).json()
recipients = [{'name': 'Paul', 'chat_id': os.environ['PAUL_TELEGRAM_CHAT_ID']},
              {'name': 'Aisling', 'chat_id': os.environ['AISLING_TELEGRAM_CHAT_ID']}]

for recipient in recipients:
    # construct the message we're going to send by examining the first few entries in the JSON forecast
    weather_message = f"Morning {recipient['name']},\n\nHere is today's forecast:\n"

    for forecast in data['list'][0:5]:
        time_as_dt = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')

        weather_message += (f"\nTime: {time_as_dt.strftime('%H:%M:%S')}\n"
                            f"Description: {forecast['weather'][0]['description'].title()}\n"
                            f"Teamperature: {int(forecast['main']['temp'])}\n"
                            f"Feels like: {int(forecast['main']['feels_like'])}\n"
                            f"Wind speed: {int(forecast['wind']['speed'] * 3.6)}Kph\n")

    # send message using the telegram API
    send_message_url = ('https://api.telegram.org/bot' + os.environ['TELEGRAM_BOT_TOKEN'] +
        '/sendMessage?chat_id=' + recipient['chat_id'] +
        '&text=' + weather_message.replace(' ', '+').replace('\n', '%0A')) # <- need to replace special characters

    requests.get(send_message_url)
