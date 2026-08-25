from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import bcrypt

from app.database.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteResponse

router = APIRouter(prefix="/api/clientes", tags=["clientes"])

@router.post("/", response_model=ClienteResponse)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    existente = db.query(Cliente).filter(Cliente.email == cliente.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    senha_bytes = cliente.senha.encode("utf-8")
    senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt()).decode("utf-8")

    novo_cliente = Cliente(
        nome=cliente.nome,
        email=cliente.email,
        senha_hash=senha_hash,
        telefone=cliente.telefone,
        endereco=cliente.endereco
    )
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente
@router.post("/login")
def login_cliente(email: str, senha: str, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.email == email).first()

    if not cliente:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    senha_bytes = senha.encode("utf-8")
    senha_hash_bytes = cliente.senha_hash.encode("utf-8")

    if not bcrypt.checkpw(senha_bytes, senha_hash_bytes):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    return {"mensagem": f"Bem-vindo, {cliente.nome}!", "id": cliente.id}