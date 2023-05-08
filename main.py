from typing import Any
from blocks.app import App

from src.processors.chat_interaction import UpdateHandler
from src.processors.keep_events import EventKeeperToMongo
from src.sources import LongPollReader
from src.policies.base import Policy
from src.policies.responses import Echo
from src.policies.channel_posts import TextPostToChannel

if __name__ == '__main__':    
    policies: list[Policy] = [
        TextPostToChannel(),
    ]
    
    blocks = [
        LongPollReader(),
        UpdateHandler(policies),
        # EventKeeperToMongo(),
    ]

    App(blocks=blocks).run(once=True)