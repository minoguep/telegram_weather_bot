# Telegram API: Building a weather bot in 30 lines of code

This is the subject of a [tutorial](https://paulminogue.com/index.php/2020/03/22/telegram-api-building-a-weather-bot-in-30-lines-of-code/)
on [my website](http://paulminogue.com). All code required is contained within [weather_bot.py](weather_bot.py) (just 30 lines of code!!).

All you will need to run this is:
- [An OpenWeatherMap API token](https://openweathermap.org/appid)
- Your OpenWeatherMap city ID
- [A telegram bot](https://core.telegram.org/bots)
- Your telegram chat ID

To automate the sending of forecasts every morning, I set up a simple cronjob on my Raspberry Pi to run at 8AM
every morning.