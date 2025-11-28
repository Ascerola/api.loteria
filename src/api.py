from fastapi import FastAPI

from routers.root import router as root_router


def register_routes(app: FastAPI) -> None:
    app.include_router(root_router)
