from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import routes


app = FastAPI()


@app.get("/")
async def home():
    return {"hello": "world"}


def setup_settings(app):
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
        allow_headers=[
            "Content-Type",
            "Set-Cookie",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Origin",
            "Authorization",
        ],
    )


def start_application():
    app = FastAPI(title="eLib")
    setup_settings(app)
    app.include_router(router=routes)
    return app


app = start_application()
