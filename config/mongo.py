from pydantic import BaseSettings, Field, MongoDsn


class MongoConf(BaseSettings):
    host: str = Field(env='MONGO_HOST')
    port: int = Field(env='MONGO_PORT', default=27017)
    base: str = Field(env='MONGO_BASE')
    user: str | None = Field(env='MONGO_USER')
    pswd: str | None = Field(env='MONGO_PASS')

    @property
    def connection_string(self) -> str:
        if self.user and self.pswd:
            return f'mongodb://{self.user}:{self.pswd}@{self.host}:{self.port}'
        elif self.user:
            return f'mongodb://{self.user}@{self.host}:{self.port}'
        else:
            return f'mongodb://{self.host}:{self.port}'