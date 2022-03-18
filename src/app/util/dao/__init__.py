from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, registry

from ...config import Config


def return_engine():
    return create_engine(Config.DB_URL)


mapper_register = registry()
Base = declarative_base()
engine = return_engine()

mapper_register.metadata.create_all(engine)
#Base.metadata.create_all(Engine)