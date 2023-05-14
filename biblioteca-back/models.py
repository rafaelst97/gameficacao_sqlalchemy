from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine, DateTime
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True, index=True)
    senha = Column(String(255))

class Livro(Base):
    __tablename__ = 'livro'
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100))
    resumo = Column(String(500))
    
class Emprestimo(Base):
    __tablename__ = 'emprestimo'
    
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    data_retirada = Column(DateTime)
    status = Column(Integer(1))
    
class item_emprestimo(Base):
    __tablename__ = 'item_emprestimo'
    
    id_livro = Column(Integer, ForeignKey('livro.id'), primary_key=True)
    id_emprestimo = Column(Integer, ForeignKey('emprestimo.id'), primary_key=True)