from fastapi import FastAPI
from routes.cinebusca import router

app = FastAPI()

app.include_router(router)
