from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "running"}

@app.post("/reset")
def reset():
    return {"state": "reset done"}

@app.get("/state")
def state():
    return {"status": "running"}

@app.post("/step")
def step(action: dict):
    return {"result": "ok", "action": action}
