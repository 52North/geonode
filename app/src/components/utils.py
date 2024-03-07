# app/utils.py
import requests

def fetch_sta_data(sta_url):
    response = requests.get(sta_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
