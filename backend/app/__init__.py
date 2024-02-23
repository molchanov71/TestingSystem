import fastapi
from .db import Base, engine

server = fastapi.FastAPI()

from .routes import *

from .models import *
Base.metadata.create_all(bind=engine)
