from fastapi import FastAPI
from BACK.routes.users import user
from FRONT.frontapp import UI

app=FastAPI(title="REST API WITH ARANGO DB",description="this is a description", version="0.0")
app.include_router(user)
app.include_router(UI)