import json

import requests

from constants import (
    USERNAME,
    URL_BASE,
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

