from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
'''
@app.delete("/users/{user_id}")
def delete(user_id:int):
    for user in users:
     if user["id"]==user_id:
        users.remove(user)
        return {"message": f"User {user_id} deleted"}
    return {"error": "User not found"}    
'''    

@app.get("/users")
def get_users():
    return users
