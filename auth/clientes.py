from fastapi import Depends , HTTPException
from auth.auth_router import auth
from sqlalchemy.orm import Session
from dependecias import pegar_sessao , verificar_token_clientes  
from schemas import LoguinCliente , LoguinCli
from models import Clientes, Usuario
from passlib.context import CryptContext
from security import bcrypt_context
from datetime import timezone , timedelta , datetime
from config import ACESS_TOKEN_MINUTES , SECRET_KEY , ALGORITHM
from jose import jwt , JWTError


def criar_token(id_cliente , duracao_token = timedelta(minutes = ACESS_TOKEN_MINUTES)):
    data_exp = datetime.now(timezone.utc) + duracao_token
    dic_inf = {"sub":str(id_cliente), "exp":data_exp}
    jwt_codificado =  jwt.encode(dic_inf, SECRET_KEY, algorithm = ALGORITHM)
    return jwt_codificado


@auth.post("/criar_conta/cliente")
async def criar_conta(loguin_clientes: LoguinCliente,session: Session=Depends(pegar_sessao)):
    cliente = session.query(Clientes).filter(Clientes.email == loguin_clientes.email).first()
    if cliente:
        raise HTTPException(status_code = 400 ,detail="cliente já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(loguin_clientes.senha)
        novo_cliente = Clientes(
            nome=loguin_clientes.nome,
            email=loguin_clientes.email,
            senha=senha_criptografada,
            telefone=loguin_clientes.telefone,
            ativo=True
        )
        session.add(novo_cliente)
        session.commit()
        return {"mensagem":f"Cliente cadastrado com sucesso {loguin_clientes.email}"}

@auth.post("/loguin/{clientes}")
async def loguin_clientes(loguin_cliente:LoguinCli,session: Session = Depends(pegar_sessao)):
    cliente = session.query(Clientes).filter(Clientes.email == loguin_cliente.email).first()
    if not cliente:
        raise HTTPException(status_code = 401 , detail = "cliente não encntrado !")
    else:
        access_token = criar_token(cliente.id)
        refresh_token = criar_token(cliente.id)
        return {
            "access_token":access_token,
            "token_type": "Bearer",
            "refresh_token":refresh_token
        }

@auth.get("/listar_clientes")
async def listar_clientes(session: Session = Depends(pegar_sessao)):
    lista = session.query(Clientes).all()
    return {
        "clientes": [
            {"id": cliente.id, "email": cliente.email}
            for cliente in lista
        ]
    }
