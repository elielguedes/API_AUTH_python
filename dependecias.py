from fastapi import Depends , HTTPException
from sqlalchemy.orm import sessionmaker , Session
from models import db , Usuario , Clientes
from jose import jwt , JWTError
from config import SECRET_KEY ,ALGORITHM 
from security import oauth2_schemas , oauth2_schemas

def pegar_sessao():
    try:
        session = sessionmaker(bind = db)
        Session = session()
        yield Session
    finally:
        Session.close()

def verificar_token(token:str = Depends(oauth2_schemas), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_usuario = int(dic_info.get("sub" , ""))
    except JWTError:
        raise HTTPException(status_code = 401 , detail="Acesso negado verifique a validade do token")
    usuario = session.query(Usuario).filter(Usuario.email == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code = 401 , detail="Acesso Invalido")
    return usuario

def verificar_token_clientes(token:str = Depends(oauth2_schemas), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code = 401 , detail="Acesso negado verifique a validade do token")
    usuario = session.query(Clientes).filter(Clientes.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code = 401 , detail="Acesso Invalido")
    return usuario
