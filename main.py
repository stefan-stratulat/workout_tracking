import requests
import os
from datetime import datetime

#Input workout info
workout = input("Tell me which exercesies you did: ")


#post workout info to Nutritionix api
headers = {
    "x-app-id": os.environ["NUTRITIONIX_APP_ID"],
    "x-app-key": os.environ["NUTRITIONIX_API_KEY"],
}

parameters = {
    "query":workout
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)

data = response.json()
print(data)

today = datetime.now()
date = today.strftime("%Y-%m-%d")
time = today.strftime("%H:%M")

rows = {
    "workout":
        {"date":date,
        "time":time,
        "exercise":(data["exercises"][0]["name"]).title(),
        "duration":data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"]
        }
}

sheety_header ={
    "Authorization":os.environ["SHEETY_API"]
}

add_rows = requests.post(url="https://api.sheety.co/7f2c9a5134d5a523511e869d5cf54025/myWorkouts/workouts",json=rows,headers=sheety_header)
print(add_rows.status_code)