from fastapi import APIRouter
from BACK.conections.arangodb import (ID_userdb,
                                Create_userdb,
                                Read_usersdb,
                                Update_userdb,
                                Delete_userdb)
from BACK.models.models import user_model
user=APIRouter()
@user.get("/users",tags=["users"])#,response_model=user_model)
def read_users():
    return Read_usersdb()
#
@user.get("/users/{id}",tags=["users"])#,response_model=user_model)
def read_user(id):
    return ID_userdb(id)
#
@user.post("/user",tags=["users"],response_model=user_model)
def create_user(user:user_model):
    new_user =  user.dict()    
    return Create_userdb(new_user)
#
@user.put("/user_update/{id}",tags=["users"],response_model=user_model)
def update_user(id,upd_user:user_model):
    update_user=upd_user.dict()
    return Update_userdb(id,update_user)
#
@user.delete("/delete_user/{id}",tags=["users"])
def delete_user(id):
    return Delete_userdb(id)