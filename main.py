from blocks.app import App

from src.sources import LongPoolReader
from src.processors import UpdateParser, ObjectSender

if __name__ == '__main__':
    blocks = [
        LongPoolReader(),
        UpdateParser(),
        ObjectSender(),
    ]

    App(blocks).run(once=True)