from typing import Callable, Any
from blocks.types.base import Processor
from loguru import logger
from tg_api.methods import send_message, send_poll
from tg_api.objects import Update

from src.events import NewObject, NewMessage, NewPoll


class UpdateParser(Processor):
    def __init__(self) -> None:
        ...

    def __call__(self, event: Update) -> NewMessage | NewPoll | None:
        logger.info(f'New update for parsing: {event.dict()}')
        
        if event.message and event.message.text == '1':
            return NewMessage(
                chat_id = event.message.chat.id,
                text = 'kek',
                reply_to_message_id = event.message.message_id,
            )


class ObjectSender(Processor):
    def __init__(self) -> None:
        self.senders: dict[Any, Callable] = {
            NewMessage: send_message,
            NewPoll: send_poll,
        }

    def __call__(self, event: NewMessage | NewPoll) -> None:
        logger.info(f'Send new event: {type(event), event.dict()}')
        eventType = type(event)
        eventSender = self.senders[eventType]
        is_done = eventSender(**event.dict())