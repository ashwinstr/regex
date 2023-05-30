# server.py

from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
async def read_root() -> str:
    return "Website is healthy."

api_port = os.environ.get("API_PORT")

if __name__ == "__main__" and api_port:
    print("Starting uvicorn")
    uvicorn.run(app, worker=1, host="0.0.0.0", api=api_port, log_level="error")
