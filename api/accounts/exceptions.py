from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi import HTTPException


unauthorized = HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
