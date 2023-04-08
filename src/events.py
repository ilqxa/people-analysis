from pydantic import BaseModel

from abc import ABC


class NewObject(ABC, BaseModel):
    ...

class NewMessage(NewObject):
    chat_id: int | str
    text: str
    reply_to_message_id: int | None = None

class NewPoll(NewObject):
    chat_id: int | str
    question: str
    options: list[str]
    is_anonymous: bool = False