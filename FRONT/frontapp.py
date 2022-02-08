from fastapi import (
                    APIRouter,
                    Request
                    )
from pydantic.types import Json
#from requests import (
                    #get,
                    #delete,
                    #put,
                    #post
                    #)

import requests as rq
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from FRONT.models import user_model

UI=APIRouter()
templates=Jinja2Templates(directory="FRONT/templates")
#List all users in the db
@UI.get("/",tags=["UI"])#,response_model=user_model)
def read_users(request:Request):
    """
    All users from db are listed with the list_all template, list_all template has the 
    structure: edit button, user name, user lastname, age, seasson  and the delete botton
    """
    db_users=rq.get("http://localhost:8000/users").json()
    db_users_keys=[*db_users]
    return templates.TemplateResponse("list_all.html",{"request":request,"users":db_users})
#New user 
@UI.get("/app/new_user",tags=["UI"])#,response_model=user_model)
def new_user(request:Request):
    """
    Render the form for creates the user into the db  mmm
    """
    return templates.TemplateResponse("new_form.html",{"request":request})

#New user user
@UI.post("/app/new_user", tags=["UI"])
async def new_user_post(request:Request):
    """get the post form with the new user info to be recorded in the db"""
    edited_user=await request.form()
    try:
        #user_post=rq.post("http://localhost:8000/user",json={**edited_user},timeout=1).json()
        #For some reason the put method put the information but take a infinity time gettin a response
        #So I can't catch the response value for the endpoint
        user_post=rq.post(f"http://localhost:8000/user",json={**edited_user},timeout=1)
    except:
        print("SALIDA: ")
    return RedirectResponse("http://localhost:8000/",303)
#delete one user
@UI.get("/app/user_del/{id}",tags=["UI"])
def delete_user(request:Request, id:int):
    """
    delete the user with id from request of list_all template, the request is a GET request but
    the end point with the backend is with DELETE method.
    """
    print("FRONT END: ",id)
    user_del = rq.delete(f"http://localhost:8000/delete_user/{id}").json()
    #print(user_del)
    if user_del["status"]=="fail":
        return user_del
    return RedirectResponse("http://localhost:8000/",303)
#edit one user
@UI.get("/app/user/{id}", tags=["UI"])
def edit_user_form(request:Request,id:int):
    """Render the template with the user information to be modified"""
    db_user=rq.get(f"http://localhost:8000/users/{id}").json()
    return templates.TemplateResponse("user_form.html", {"request":request, "user_id":id, "user":db_user})
@UI.post("/app/user/{id}", tags=["UI"])
async def edit_user_post(request:Request,id:int):
    """get the post form with the update user info to be recorded in the db"""
    edited_user=await request.form()
    try:
        #user_post=rq.post("http://localhost:8000/user",json={**edited_user},timeout=1).json()
        #For some reason the put method put the information but take a infinity time gettin a response
        #So I can't catch the response value for the endpoint
        user_post=rq.put(f"http://localhost:8000/user_update/{id}",json={**edited_user},timeout=1)
    except:
        print("SALIDA: ")
    return RedirectResponse("http://localhost:8000/",303)

#create new user