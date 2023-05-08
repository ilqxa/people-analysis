from pydantic import BaseSettings, Field


class AllowedChats(BaseSettings):
    admin_chat_id: int = Field(env='TG_ADMIN_CHAT_ID')
    main_channel_id: int = Field(env='TG_MAIN_CHANNEL_ID')