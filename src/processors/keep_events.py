from blocks.types.base import Processor

from tg_api.objects import Update


class EventKeeperToMongo(Processor):
    def __init__(self) -> None:
        ...

    def __call__(self, event: Update) -> None:
        ...