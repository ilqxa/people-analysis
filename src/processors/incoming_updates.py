from typing import Callable, Any
from blocks.types.base import Processor
from loguru import logger
from tg_api.methods import *
from tg_api.objects import Update, Message, InlineKeyboardMarkup, InlineKeyboardButton


class UpdateHandler(Processor):
    def __init__(self) -> None:
        ...

    def __call__(self, event: Update) -> None:
        logger.info(f'New update for parsing: {event.dict()}')
        
    
    def forward_message_to_admins(self, msg: Message) -> None:
        pass