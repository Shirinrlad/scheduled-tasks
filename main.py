# twilio reference number/recovery = KBQUUMZ1XDCKD5V8NH75Y8DL

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0a251aef39e2fbba97a6c381a57b247e"
account_sid = "ACd9752922e09badfdf83bc7b8b921ba98"
auth_token = "16f1f1c1a260f582c1ce2b2c6593a82d"
client = Client(account_sid, auth_token)

weather_prams = {
    "lat": 13.3409,
    "lon": 74.7421,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_prams)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "Its raining",
        to = "whatsapp:+919819881688",
        from_ = "whatsapp:+14155238886"
        # '+15705310127'
    )
    print(message.status)
