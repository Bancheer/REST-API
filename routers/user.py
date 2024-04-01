from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user as UserService
from contacts import user as UserContact

router = APIRouter()
@router.post('/', tags=['user'])
async def create(data: UserContact.User, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', tags=['user'])
async def get_user(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.get('/name/{name}', tags=['user'])
async def get_users_by_name(name: str, db: Session = Depends(get_db)):
    return UserService.get_users_by_name(name, db)

@router.get('/last_name/{last_name}', tags=['user'])
async def get_users_by_last_name(last_name: str, db: Session = Depends(get_db)):
    return UserService.get_users_by_last_name(last_name, db)

@router.get('/email/{email}', tags=['user'])
async def get_users_by_email(email: str, db: Session = Depends(get_db)):
    return UserService.get_users_by_email(email, db)


@router.get('/', tags=['user'])
async def get_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)


@router.put('/{id}', tags=['user'])
async def update(id: int = None, data: UserContact.User = None, db: Session = Depends(get_db)):
    return UserService.update_user(data, db, id)

@router.delete('/{id}', tags=['user'])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.delete_user(id, db)

@router.get('/user/{birthday}', tags=['user'])
async def birthday_seven(db: Session = Depends(get_db)):
    return UserService.birthday_seven(db)