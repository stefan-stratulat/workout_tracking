import requests
import os

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
print(response.text)