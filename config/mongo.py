from pydantic import BaseModel, Field, MongoDsn


class MongoConf(BaseModel):
    host: str = Field(env='MONGO_HOST')
    port: int = Field(env='MONGO_PORT', default=27017)
    user: str | None = Field(env='MONGO_USER', default=None)
    pswd: str | None = Field(env='MONGO_PASS', default=None)

    @property
    def connection_string(self) -> MongoDsn:
        return MongoDsn(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.pswd,
        )