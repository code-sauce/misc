import requests
import json

app_id = '1501474760160377'
app_secret = '809d3767063098f58e2055a5657cf8d9'
picturewicture_fb_page_id = '456535774506257'
params = {
    'client_id': app_id,
    'client_secret': app_secret,
    'grant_type': 'client_credentials'
}
access_token = "CAAVVlVW39HkBALpqwWYt5sp3KRVXdpkx6IrwT8C0ZB4Jnlq78Kto7mN14divVxtJGTsPJKaBdzGbAx3Nuk7UNcRL18PZA3o2F3lM6S5a51pOxAlzeP1eZArfRSP0NnScAIVStCzcLbw4Pcv9dZAikIXdMhLioj52GP6D3NVsuioZAI0FEASgImSrfFvurVihUkatqya1ifgZDZD"

# response = requests.get(
#     'https://graph.facebook.com/me/accounts',
#      params={'access_token': '%s' % access_token}
# )

# get the page access token
# url = 'https://graph.facebook.com/%s' % picturewicture_fb_page_id
# response = requests.get(url, params={'fields': 'access_token', 'access_token': access_token})
# page_access_token = response.json().get('access_token')

group_id = '390918484357067'  # moms photography group
post_id = '525228457636988'
url = 'https://graph.facebook.com/%s/feed' % group_id

response = requests.post(url, params={'message': 'Hello', 'access_token': access_token})
print response.text

