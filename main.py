from fastapi import FastAPI
from pydantic import BaseModel
from workflow import run_workflow

app = FastAPI()

class Request(BaseModel):
    user_input: str

@app.get("/")
def root():
    return {"msg": "Multi-Agent System Running"}

@app.post("/run")
def run(req: Request):
    return run_workflow(req.user_input)
