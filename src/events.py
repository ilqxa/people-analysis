from __future__ import annotations

from abc import ABC

from pydantic import BaseModel

from tg_api.objects import InlineKeyboardMarkup


class NewMessage(BaseModel):
    chat_id: int | str
    text: str
    reply_to_message_id: int | None
    reply_markup: InlineKeyboardMarkup | None

class NewPoll(BaseModel):
    chat_id: int | str
    question: str
    options: list[str]
    is_anonymous: bool = False

class NewCallbackAnswer(BaseModel):
    callback_query_id: str
    text: str | None
    show_alert: bool = True

NewObject = NewMessage | NewPoll | NewCallbackAnswer