from fastapi import FastAPI
from databases import Database

DATABASE_URL = "postgresql://user:password@db:5432/database"

app = FastAPI()
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/api")
async def read_root():
    return {"message": "Hello World"}
