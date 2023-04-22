from config.mongo import MongoConf


def test_mongo_conf() -> None:
    mc = MongoConf()
    assert mc.host == 'localhost'