import pkgutil
from importlib import import_module
from typing import Tuple

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config import DATABASE_URL
from db.models import Base

_engine = None
_SessionLocal: sessionmaker | None = None


def _import_models() -> None:
    """
    Import all modules in db.models so that SQLAlchemy sees mapped classes.
    Safe to call multiple times.
    """
    try:
        import db.models as models_pkg
    except ModuleNotFoundError:
        return

    for module in pkgutil.iter_modules(models_pkg.__path__):
        import_module(f"{models_pkg.__name__}.{module.name}")


def init_engine_and_schema() -> Tuple[object, sessionmaker]:
    """
    Create the engine, import models, and run automigration (create_all).
    Returns (engine, SessionLocal). Subsequent calls reuse the same objects.
    """
    global _engine, _SessionLocal

    if _engine is None:
        _engine = create_engine(DATABASE_URL, future=True)
        _import_models()
        Base.metadata.create_all(bind=_engine)
        _SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False, future=True)

    if _SessionLocal is None:
        raise RuntimeError("Session factory not initialized")

    return _engine, _SessionLocal


def get_session() -> Session:
    """Convenience helper to get a Session after ensuring schema is created."""
    _, SessionLocal = init_engine_and_schema()
    return SessionLocal()
