from fastapi import FastAPI

from app.router import router as router_rps

description = """
App API helps you do awesome stuff. 🚀

## Hello

Say **Hello What is love**.

## Rps

You will be able to play in rock paper scissors
"""

tags_metadata = [
    {
        "name": "hello",
        "description": "Say Hello What is love",
    },
    {
        "name": "rps",
        "description": "You will be able to play in rock paper scissors",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app = FastAPI(
    title="App",
    description=description,
    version="0.0.1",
    contact={
        "name": "MKurziankou",
        "email": "MKurzenkov.otd14@gmail.com",
    },
    openapi_tags=tags_metadata
)


@app.get("/hello", tags=["hello"])
def say_hello():
    return {"message": "Hello What is love"}


app.include_router(router_rps)
