import requests

def fetch(url):
    res = requests.get(url=url)
    return res.text