from typing import List  
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
class UsuarioCreate(UsuarioBase):
    senha: str
class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
class PaginatedUsuario(BaseModel):
    limit: int
    offset: int
    data: List[Usuario]