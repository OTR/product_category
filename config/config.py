from pydantic_settings import SettingsModel

class DatabaseSettings(SettingsModel):
    DATABASE_URL: str

def get_database_config():
    """"""
