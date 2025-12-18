from sqlalchemy import create_engine , Column , String , Integer , ForeignKey , Float , Boolean , Date
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///Banco.db", connect_args={"check_same_thread":False})

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column("id", Integer , primary_key = True , autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean)

    def __init__(self, nome , email , senha , ativo=True , admin=True):
        self.nome = nome
        self.email = email 
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


class Clientes(Base):
    __tablename__ = "clientes"

    id =Column("id" ,Integer , primary_key = True , autoincrement = True)
    nome = Column("nome" , String)
    email = Column("email" , String)
    senha = Column("senha" , String)
    telefone = Column("telefone", Integer)
    ativo = Column("ativo", Boolean)

    def __init__(self , nome , email , senha , telefone , ativo):
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.telefone = telefone 
        self.ativo = ativo

class servicos(Base):
    __tablename__ = "Servicos"

    id =Column("id" ,Integer , primary_key = True , autoincrement = True)
    clientes = Column("clientes", ForeignKey("clientes.id"))
    nome = Column("nome" , String)
    descricao = Column("descrecao", String)
    preco = Column("preco" , Float)
    duracao_min = Column("duracao_min" , Date)
    ativo = Column("ativo" , Boolean)
    novo_horario = Column("novo_horario" , Date)

    def __init__(self , clientes , nome , descricao , preco , duracao_min , ativo , novo_horario):
        self.clientes = clientes
        self.nome = nome
        self.descricao = descricao
        self.preco = preco 
        self.duracao_min = duracao_min
        self.ativo = ativo 
        self.novo_horario = novo_horario

