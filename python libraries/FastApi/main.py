from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


users=[
    {"id":1,"name":"hammad","marks":80},
    {"id":2,"name":"Ali","marks":70},
    {"id":3,"name":"Ahmed","marks":90},
    {"id":4,"name":"Zaid","marks":60}
]

@app.post("/users")
def post_grade():
    if user["marks"] == 90:
            user["grade"] = "A+"
    elif user["marks"] == 80:
            user["grade"] = "A"
    elif user["marks"] == 70:
            user["grade"] = "B"
    elif user["marks"] == 60:
            user["grade"] = "C"

    return users   

@app.get("/users")
def root():
    return users

@app.get("/user/{user_id}")
def user(user_id:int):
    user_found=False
    for us in users:
        if us["id"]==user_id:
            user_found=True
            return us
    if user_found==False:
       return "User do not Found"     
    