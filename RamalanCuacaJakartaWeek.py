import datetime
import requests

url = 'https://api.openweathermap.org/data/2.5/onecall?lat=-6.2146&lon=106.8451&units=metric&exclude=current,minutely,hourly,alerts&appid=ae34db5320ecc0ae7e2fa5c9864bf7cc'
r = requests.get(url)
response = r.json()

print("Weather Forecast:")
date = datetime.datetime.today()
for temp in response['daily']:
    date += datetime.timedelta(days=1)
    print("{}{}°C".format(date.strftime("%a, %d %b %Y: "), temp['temp']['day']))