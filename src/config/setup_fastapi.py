from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_fastapi() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "https://sim-stock-be.vercel.app/",
            "https://sim-stock-fe.vercel.app/",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
