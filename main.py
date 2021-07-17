import json

import requests

from constants import (
    USERNAME,
    URL_BASE,
    GRAPH_ID,
    GRAPH_URL,
)
from secrets import API_TOKEN


def create_user():
    data = {
        "token": API_TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    url = f"{URL_BASE}"
    response = requests.post(url, data=json.dumps(data))


def create_graph():
    data = {
        "id": GRAPH_ID,
        "name": GRAPH_ID,
        "unit": "commit",
        "type": "int",
        "color": "shibafu",
    }
    url = f"{URL_BASE}/{USERNAME}/graphs"
    headers = {
        "X-USER-TOKEN": API_TOKEN,
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print(f"Graph created, pleas check at {GRAPH_URL}")
    else:
        print("Graph creation failed")


# create_user()
create_graph()
