from starlette.config import Config
from datetime import timedelta
from databases import DatabaseURL
from starlette.datastructures import Secret

config = Config(".env")

ENVIRONMENT: str = config("ENVIRONMENT", cast=str, default="development")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
TESTING: bool = config("TESTING", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="NOTVERYSECRET")
JWT_ALGORITHM: str = config("JWT_ALGORITHM", cast=str, default="HS256")
ACCESS_TOKEN_EXPIRES: timedelta = config("ACCESS_TOKEN_EXPIRES", default=timedelta(hours=24))
REFRESH_TOKEN_EXPIRES: timedelta = config("REFRESH_TOKEN_EXPIRES", default=timedelta(days=5))
DATABASE_URL: DatabaseURL = config("DATABASE_URL", cast=DatabaseURL, default="postgresql://localhost/contenter")


if TESTING:
    DATABASE_URL = DATABASE_URL.replace(database=DATABASE_URL.database + "_test")
