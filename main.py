import json
from datetime import datetime

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


def post_value_to_graph(date=datetime.today(), quantity=1):
    formatted_date = date.strftime("%Y%m%d")
    data = {
        "date": formatted_date,
        "quantity": str(quantity),
    }
    headers = {
        "X-USER-TOKEN": API_TOKEN,
    }
    response = requests.post(GRAPH_URL, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print(f"Graph updated, pleas check at {GRAPH_URL}")
    else:
        print("Graph update failed")


# create_user()
# create_graph()
post_value_to_graph()
