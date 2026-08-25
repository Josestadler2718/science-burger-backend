from pydantic import BaseModel, EmailStr

class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: str | None = None
    endereco: str | None = None

class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        from_attributes = True