from typing import Any

from tg_api.objects import Update
from tg_api.methods import send_message

from config.chats import AllowedChats
from src.policies.base import Policy

conf = AllowedChats()


class TextPostToChannel(Policy):
    def apply_to(self, o: Update) -> bool:
        if not isinstance(o, Update): return False
        if not o.message: return False
        if not o.message.text: return False
        if o.message.chat.id != conf.admin_chat_id: return False
        return send_message(
            chat_id = conf.main_channel_id,
            text = o.message.text,
        )