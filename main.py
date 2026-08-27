from fastapi import FastAPI

app = FastAPI(
    title="Basic FastAPI App",
    description="A simple FastAPI assignment project",
    version="1.0.0",
)
@app.get("/")
def home():
    return {
        "message": "Hello, FastAPI!"
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "message": f"Hello, {name}!",
        "name": name
    }