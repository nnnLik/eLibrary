from decouple import config


DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", ""),
        "NAME": config("POSTGRES_DB", ""),
        "USER": config("POSTGRES_USER", ""),
        "PASSWORD": config("POSTGRES_PASSWORD", ""),
        "HOST": config("POSTGRES_HOST", ""),
        "PORT": config("POSTGRES_PORT", ""),
    }
}
