# twilio reference number/recovery = KBQUUMZ1XDCKD5V8NH75Y8DL

import requests
from twilio.rest import Client



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
