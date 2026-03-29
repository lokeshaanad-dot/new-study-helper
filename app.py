import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "running"}

@app.post("/reset")
def reset():
    return {"state": "reset"}

@app.post("/step")
def step():
    return {"state": "step"}

@app.get("/state")
def state():
    return {"state": "running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
