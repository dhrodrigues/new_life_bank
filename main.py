from ast import Delete
from pydantic import BaseModel, Field
import uvicorn
from typing import Dict,Optional
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

accounts = []

class Account(BaseModel):
    id: int
    nome: str
    documento: str
    dataNacimento: str
    email: str
    telefone: str

@app.get("/")
def root() -> str:
    return "Jujubinha"

@app.get("/health")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.post("/accounts", response_model=bool, tags=["accounts"])
def create_account(account: Account):

    accounts.append(account)
    
    return True

@app.get("/accounts", response_model=list, tags=["accounts"])
def list_account():
    return  accounts

@app.get("/accounts/{id}", response_model=Optional[Account], tags=["accounts"])
def get_account(id: int):
    for account in accounts:
        if account.id == id:
            return account

    return None

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
    