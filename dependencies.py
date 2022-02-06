import random

from uuid import uuid4
from datetime import datetime


def isValidName(name: str) -> bool:
    return bool(name)

def getCurrentTime() -> str:
    return datetime.now().strftime("%Y/%m/%d %H:%M")

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