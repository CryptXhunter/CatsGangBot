from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    SLEEP_TIME: list[int] = [7200, 10800]
    START_DELAY: list[int] = [5, 25]
    AUTO_TASK: bool = True
    JOIN_TG_CHANNELS: bool = True
    REF_ID: str = 'tU1c2BRmdm4h46hs8FXDO'
    DISABLED_TASKS: list[str] = ['INVITE_FRIENDS', 'TON_TRANSACTION', 'BOOST_CHANNEL', 'ACTIVITY_CHALLENGE']


settings = Settings()
