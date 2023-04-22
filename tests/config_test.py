from config.mongo import MongoConf


def test_mongo_conf():
    mc = MongoConf()
    assert mc.host == 'localhost'