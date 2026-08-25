from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes import clientes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clientes.router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import Base, engine
from app.routes import clientes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois trocar por endereço específico do site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router)