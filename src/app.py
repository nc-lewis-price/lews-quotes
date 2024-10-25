from fastapi import FastAPI

app = FastAPI()


@app.get("/api/healthcheck")
def get_healthcheck():
    return {"msg": "all good!"}
