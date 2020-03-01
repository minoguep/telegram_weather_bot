# A simple weather bot using OpenWeatherMap and Telegram APIs

This will be the subject of a future tutorial on [my website](http://paulminogue.com). All code required is contained
within [weather_bot.py](weather_bot.py (just 30 lines of code!!).30

All you will need to run this is:
- [An OpenWeatherMap API token](https://openweathermap.org/appid)
- Your OpenWeatherMap city ID
- [A telegram bot](https://core.telegram.org/bots)
- Your telegram chat ID

To automate the sending of forecasts every morning, I set up a simple cronjob on my Raspberry Pi to run at 8AM
every morning.