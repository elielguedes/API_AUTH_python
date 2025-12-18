from fastapi import APIRouter , Depends , HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import Usuario 
from schemas import usuario , LoguinSchemas
from dependecias import pegar_sessao , verificar_token
from sqlalchemy.orm import Session 
from config import SECRET_KEY , ALGORITHM , ACESS_TOKEN_MINUTES
from security import bcrypt_context
from datetime import timedelta , timezone , datetime
from jose import jwt

auth = APIRouter(prefix="/auth" , tags=['auth'])

def criar_token(id_usuario , duracao_token = timedelta(minutes = ACESS_TOKEN_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token #datatime.now mostra data e horas atuais já timezone fuzo horario de um datetime 
    dic_info = {"sub":str(id_usuario) , "exp":data_expiracao} # um dicionario de informações com informações do usuario e a data do token 
    jwt_codificado = jwt.encode(dic_info , SECRET_KEY ,algorithm = ALGORITHM)
    return jwt_codificado

def autenticar(email , senha , session:Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if not usuario:
        return False 
    elif not bcrypt_context.verify(senha , usuario.senha):
        return False
    return usuario

@auth.post("/criar_conta")
async def criar_conta_user(usuario_schemas:usuario , session: Session = Depends(pegar_sessao)):
    user = session.query(Usuario).filter(Usuario.email == usuario_schemas.email).first()
    if user:
        raise HTTPException(status_code = 400 , detail="usuario já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schemas.senha)
        novo_usuario = Usuario(nome = usuario_schemas.nome , email = usuario_schemas.email ,senha = senha_criptografada, ativo =True , admin=True)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuario cadastrado com sucesso {usuario_schemas.email}"}

@auth.post("/loguin")
async def loguin(loguin_schemas:LoguinSchemas , session: Session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == loguin_schemas.email).first()
    if not usuario:
        raise HTTPException(status_code = 400 , detail="Usuario não encontrado")
    else:
        acess_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id)
        return {
            "access_token":acess_token,
            "refresh_token":refresh_token
        }
@auth.post("/loguin-form")
async def loguin_form(dados_formulario:OAuth2PasswordRequestForm = Depends() , session: Session=Depends(pegar_sessao)):
    usuario = autenticar(dados_formulario.username , dados_formulario.password ,session)
    if not usuario:
        raise HTTPException(status_code = 400 , detail="Usuario não encontrado")
    else:
        acess_token = criar_token(usuario.id)
        return {
            "access_token":acess_token,
        }

@auth.get("/refresh")
async def refresh(usuario: Usuario = Depends(verificar_token)):
    acess_token = criar_token(usuario.id)
    return {
        "access_token":acess_token,
        "token_type":"Bearer"
    }
