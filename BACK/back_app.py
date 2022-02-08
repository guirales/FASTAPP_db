from fastapi import FastAPI
from routes.users import user

app=FastAPI(title="REST API WITH ARANGO DB",description="this is a description", version="0.0")
app.include_router(user)

