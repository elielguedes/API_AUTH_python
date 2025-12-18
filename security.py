from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth2_schemas = OAuth2PasswordBearer(tokenUrl="auth/loguin-form")
bcrypt_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")

