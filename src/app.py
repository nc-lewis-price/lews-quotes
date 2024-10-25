from random import randint
from fastapi import FastAPI
from data.data import quotes

app = FastAPI()


@app.get("/api/healthcheck")
def get_healthcheck():
    return {"msg": "all good!"}

@app.get("/api/random")
def get_random():
    rand_index = randint(0, len(quotes) -1)
    rand_quote = quotes[rand_index]

    return {
        "quote": {
            **rand_quote,
            "length": len(rand_quote["content"])
        }
    }
