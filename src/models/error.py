from dataclasses import dataclass
from enum import Enum


class ErrorType(int, Enum):
    MESSAGE = 1
    FIELD_LIST = 2


@dataclass
class ErrorField:
    field: str
    location: list
    message: str
    type: str


class ErrorModel:
    def __init__(self, content, _type: int):
        self.type = ErrorType(_type)

        if self.type == ErrorType.MESSAGE:
            self.content = str(content)
        elif self.type == ErrorType.FIELD_LIST:
            self.content = [ErrorField(**field) for field in content]
