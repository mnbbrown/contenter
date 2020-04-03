from typing import List
from sqlalchemy.orm import Session
from api.accounts.models import User


def get_user(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email.lower()).first()


def get_user_by_id(db: Session, user_id: str, only_active: bool = False) -> User:
    query = db.query(User).filter(User.public_id == user_id)
    if only_active:
        query = query.filter(User.disabled == False)
    return query.first()


def create_user(db: Session, email: str, password: str) -> User:
    user = User(email, password)
    db.add(user)
    db.flush()
    return user
