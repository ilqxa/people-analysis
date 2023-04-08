from blocks.types.base import Source

from tg_api.objects import Update
from tg_api.methods import get_updates


class LongPoolReader(Source):
    def __init__(self) -> None:
        pass

    def __call__(self) -> list[Update]:
        return get_updates()