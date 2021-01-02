from fastapi import FastAPI

from db.controller import list_users

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def hit_db():
    list_users()
    return {"status": "ok"}