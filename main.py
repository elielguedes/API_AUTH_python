from fastapi import FastAPI
from auth.clientes import auth
from order_router import order
from auth.clientes import auth as clientes_router

app = FastAPI()


app.include_router(auth)
app.include_router(clientes_router)
app.include_router(order)