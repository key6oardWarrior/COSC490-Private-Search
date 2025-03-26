from json import loads, dumps
from typing import Any

def serialize(data: Any) -> bytes:
    return loads(data)

def deserialize(data: bytes) -> Any:
    return dumps(data)