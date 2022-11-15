from fastapi import FastAPI
from datetime import datetime
app = FastAPI()

@app.get("/")
def welcome():
    return {'message':"Welcome to service!"}
