from typing import Any

from src.policies.base import Policy
from config.chats import AllowedChats
from tg_api.objects import Update
from tg_api.methods import send_message


conf = AllowedChats()


class Echo(Policy):
    def apply_to(self, o: Update) -> bool:
        if not isinstance(o, Update): return False
        if not o.message: return False
        if not o.message.text: return False
        if o.message.chat.id != int(conf.admin_chat_id): return False
        return send_message(
            chat_id = o.message.chat.id,
            text = o.message.text,
            reply_to_message_id = o.message.message_id,
        )