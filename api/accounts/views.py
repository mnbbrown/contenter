from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.database import get_db
from api.accounts import types, service, exceptions

router = APIRouter()


@router.post("/token", response_model=types.Credentials)
def get_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise exceptions.unauthorized
    access_token = service.create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "refresh_token": ""}


@router.get("/users/me")
def get_user():
    return {}


@router.patch("/users/me")
def update_user():
    return {}
