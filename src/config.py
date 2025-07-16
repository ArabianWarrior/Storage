from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str 
    DB_PASS: str

    RDS_HOST: str
    RDS_PORT: int 

    @property
    def REDIS_URL(self):
        return f"redis://{self.RDS_HOST}:{self.RDS_PORT}"

    @property
    def DB_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
