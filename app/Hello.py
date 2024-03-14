from fastapi import FastAPI

app = FastAPI()

@app.get("/name/{name}")
async def root(name: str):
    return {"Hello": name}

# git test1