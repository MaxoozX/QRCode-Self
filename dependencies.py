import random
import json

from uuid import uuid4, UUID
from datetime import datetime

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def isValidName(name: str) -> bool:
    return bool(name)

def getCurrentTime() -> str:
    return datetime.now().strftime("%Y/%m/%d %H:%M")

def compute_query_string(query_string: str) -> dict[str, str]:
    return dict([param.split("=") for param in query_string.split("&")])

def dummyData():

    table = []

    for _ in range(8):
        table.append({
            "ID": uuid4(),
            "time": getCurrentTime(),
            "firstname": random.choice(["Martin", "Jack", "Xiyao", "Momo", "Paulo"]),
            "lastname": random.choice(["Dubois", "Robinet", "Wan", "Laplace", "Ricko"]),
            "classID": random.choice(["1C", "BTS 1", "2D", "1A", "TB"]),
        })

    return table