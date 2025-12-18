from pydantic import BaseModel
from typing import Optional
from datetime import datetime , timezone

class usuario(BaseModel):
    nome:str
    email:str 
    senha:str
    ativo:Optional[bool]
    admin:Optional[bool]

    class config:
        from_attributes = True

class LoguinSchemas(BaseModel):
    email:str
    senha:str

    class config:
        from_attributes = True

class LoguinCliente(BaseModel):
    nome:str
    email:str
    senha:str
    telefone:int

    class config:
        from_attributes = True

class LoguinCli(BaseModel):
    email:str
    senha:str

    class config:
        from_attributes = True

class servicos_schemas(BaseModel):
    clientes:str
    nome:str
    descricao:str
    preco:float
    duracao_min:datetime
    ativo:Optional[bool] 
    novo_horario:datetime

    class config:
        from_attributes = True
