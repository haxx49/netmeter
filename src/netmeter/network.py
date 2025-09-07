import requests

def isConn():
    try:
        r = requests.get("https://www.google.com")
        if r.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False
