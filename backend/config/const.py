from decouple import config

DB_NAME = config("POSTGRES_DB")
DB_PASS = config("POSTGRES_PASSWORD")
DB_USER = config("POSTGRES_USER")
DB_PORT = config("POSTGRES_PORT")
DB_HOST = config("POSTGRES_HOST")

SECRET_AUTH = config("SECRET_AUTH")
