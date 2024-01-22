import requests

url = 'http://localhost:9696/predict'

flower_classification = {
    "url" : "https://cdn.jwplayer.com/v2/media/C5w8jfIE/poster.jpg?width=720"
}

response  = requests.post(url,json=flower_classification).json()

print(response['flower_type'])