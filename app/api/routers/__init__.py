from fastapi import Depends

from ..security import api_key_checker
from .emails import router as emails_router


def configure(app, settings):
    app.include_router(
        emails_router,
        tags=["emails"],
        prefix="/api/v1",
        dependencies=[Depends(api_key_checker)],
    )
