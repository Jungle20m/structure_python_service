from starlette.config import Config


VERSION = "1.0"

API_PREFIX = "/point"

JWT_TOKEN_PREFIX = "jwt_token"

config = Config(".env")

DATABASE_URL: str = config("DATABASE_URL")

PROJECT_NAME: str = config("PROJECT_NAME")