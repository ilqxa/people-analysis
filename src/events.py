from __future__ import annotations

from abc import ABC

from pydantic import BaseModel


class NewMessage(BaseModel):
    chat_id: int | str
    text: str
    reply_to_message_id: int | None = None

class NewPoll(BaseModel):
    chat_id: int | str
    question: str
    options: list[str]
    is_anonymous: bool = False

NewObject = NewMessage | NewPoll