from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import user as UserRouter


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(UserRouter.router, prefix='/user')