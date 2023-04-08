from blocks.app import App

from src.sources import LongPoolReader
from src.processors import UpdateHandler, ObjectSender

if __name__ == '__main__':
    blocks = [
        LongPoolReader(),
        UpdateHandler(),
        ObjectSender(),
    ]

    App(blocks=blocks).run(once=True)   #type: ignore