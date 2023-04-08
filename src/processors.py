from typing import Callable, Any
from blocks.types.base import Processor
from loguru import logger
from tg_api.methods import send_message, send_poll, answer_callback_query
from tg_api.objects import Update, Message, InlineKeyboardMarkup, InlineKeyboardButton

from src.events import NewObject, NewMessage, NewPoll, NewCallbackAnswer


class UpdateHandler(Processor):
    def __init__(self) -> None:
        ...

    def __call__(self, event: Update) -> list[NewObject]:
        logger.info(f'New update for parsing: {event.dict()}')
        
        return []
    
    def forward_message_to_admins(self, msg: Message) -> NewMessage:
        pass


class ObjectSender(Processor):
    def __init__(self) -> None:
        self.senders = {
            NewMessage: send_message,
            NewPoll: send_poll,
            NewCallbackAnswer: answer_callback_query,
        }

    def __call__(self, event: NewObject) -> None:
        logger.info(f'Send new event: {type(event), event.dict()}')
        eventType = type(event)
        eventSender = self.senders[eventType]
        is_done = eventSender(**event.dict(exclude_none=True))