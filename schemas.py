from pydantic import BaseModel , EmailStr , Field
from typing import Annotated
from datetime import datetime , timezone

class usuario(BaseModel):
    nome: Annotated[str , Field(max_length = 100)]
    email: EmailStr
    senha: Annotated[str , Field(max_length = 100)]
    ativo: bool
    admin: bool

    class config:
        from_attributes = True

class LoguinSchemas(BaseModel):
    email: EmailStr
    senha: Annotated[str , Field(max_length = 100)]

    class config:
        from_attributes = True

class LoguinCliente(BaseModel):
    nome: Annotated[str , Field(max_length = 100)]
    email: EmailStr
    senha: Annotated[str , Field(max_length = 100)]
    telefone: Annotated[str , Field(max_length = 15)]

    class config:
        from_attributes = True

class LoguinCli(BaseModel):
    email: EmailStr
    senha: Annotated[str , Field(max_length = 100)]

    class config:
        from_attributes = True

class servicos_schemas(BaseModel):
    clientes: Annotated[str , Field(max_length = 100)]
    nome: Annotated[str , Field(max_length = 100)]
    descricao: str
    preco: Annotated[float , Field(max_length = 100)]
    duracao_min: datetime
    ativo: bool
    novo_horario: datetime

    class config:
        from_attributes = True
