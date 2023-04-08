from src.sources import LongPoolReader
from tg_api.methods import send_poll


def test_long_pool() -> None:
    s = LongPoolReader()
    objs = s()
    assert True

def test_send_poll() -> None:
    res = send_poll(
        chat_id = 101232786,
        question = 'Вопрос4',
        options = ['Ответ7', 'Ответ8'],
        is_anonymous = False,
    )
    assert True