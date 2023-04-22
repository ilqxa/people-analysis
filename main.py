from blocks.app import App

from src.sources import LongPoolReader
from src.processors.incoming_updates import UpdateHandler

if __name__ == '__main__':
    blocks = [
        LongPoolReader(),
        UpdateHandler(),
    ]

    App(blocks=blocks).run(once=True)   #type: ignore