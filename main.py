from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class UserCreate(BaseModel):
    name: str

@app.post("/users")
def create_user(user: UserCreate):
    user_id = len(users) + 1
    new_user = {
        "id": user_id,
        "name": user.name
    }
    users.append(new_user)
    return new_user

@app.get("/users")
def get_users():
    return users
