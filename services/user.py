from datetime import datetime, timedelta
from sqlalchemy import cast, Date
from models.user import User
from sqlalchemy.orm import Session
from contacts import user

def create_user(data: user.User, db: Session):
    user = User(**data.model_dump(exclude_unset=True))
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print("e")
    return user

def get_user(id: int, db:Session):
    return db.query(User).get(id)

def get_users_by_name(name: str, db: Session):
    return db.query(User).filter(User.name == name).all()

def get_users_by_last_name(last_name: str, db: Session):
    return db.query(User).filter(User.last_name == last_name).all()

def get_users_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).all()

def get_users(db: Session):
    return db.query(User).all()

def update_user(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if user:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user

def birthday_seven(db: Session):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    users = db.query(User).filter(cast(User.birthday, Date) >= today, cast(User.birthday, Date) <= next_week).all()
    if not users:
        return {"message": "There are no users with birthdays in the next 7 days."}
    return users