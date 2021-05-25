import config
import gather_keys as Oauth2
import fitbit
from datetime import datetime, timedelta
import requests
import time

def generate_metric(ts, bmi, fat_percent, steps, sleep, workout, water, heart_rate, bp):
    return {
        "@timestamp": ts.strftime("%Y-%m-%dT%H:%M:%S"),
        "payload": {
            "bmi": bmi,
            "fat": fat_percent,
            "steps": steps,
            "sleep": sleep,
            "workout": workout,
            "water_glasses": water,
            "avg_heartrate": heart_rate,
            "blood_pressure": bp
        }
    }

def report_to_elastic(metric):
    client = requests.post("http://elasticsearch:9200/fitops/_doc", json=metric)
    return client.content

CLIENT_ID = config.oauth2_client_id
CLIENT_SECRET = config.client_secret


server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)


start_date = datetime.now()

## fetching last 31 days worth of data from fitbit
for i in range(0, 31):
    current_ts = start_date + timedelta(days=i)
    todays_data = auth2_client.intraday_time_series('activities/*', base_date=current_ts, detail_level='1sec')

    bmi = todays_data["payload"]["fat"]["bmi"]
    fat = todays_data["payload"]["fat"]["value"]
    steps = todays_data["payload"]["workout"]["steps"]["count"]
    sleep = todays_data["payload"]["sleep"]["duration"]*60
    workout = todays_data["payload"]["workout"]["duration"]*60
    water = todays_data["payload"]["diet"]["water"]["glasses"]
    avg_heart_rate = todays_data["payload"]["cardiac_health"]["heart_rate"]
    avg_bp = todays_data["payload"]["cardiac_health"]["blood_pressure"]["systolic"]

    metric = generate_metric(current_ts, bmi, fat, steps, sleep, workout, water, avg_heart_rate, avg_bp)

## An loop which runs every day to capture fitbit's data of the current data and report it to elasticsearch

while (True):
    today_ts = datetime.now()

    todays_data = auth2_client.intraday_time_series('activities/*', base_date=current_ts, detail_level='1sec')

    bmi = todays_data["payload"]["fat"]["bmi"]
    fat = todays_data["payload"]["fat"]["value"]
    steps = todays_data["payload"]["workout"]["steps"]["count"]
    sleep = todays_data["payload"]["sleep"]["duration"]*60
    workout = todays_data["payload"]["workout"]["duration"]*60
    water = todays_data["payload"]["diet"]["water"]["glasses"]
    avg_heart_rate = todays_data["payload"]["cardiac_health"]["heart_rate"]
    avg_bp = todays_data["payload"]["cardiac_health"]["blood_pressure"]["systolic"]

    metric = generate_metric(current_ts, bmi, fat, steps, sleep, workout, water, avg_heart_rate, avg_bp)

    # Wait for 24 hours to run again
    time.sleep(86400)
