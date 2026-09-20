from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.user import UserCreate, UserUpdate, UserRead
from pos.services import user as user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead, summary="Create a new user")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)


@router.get("/", response_model=list[UserRead], summary="List all users")
def list_users(db: Session = Depends(get_db)):
    return user_service.list_users(db)


@router.get("/username/{username}", response_model=UserRead, summary="Get a user by username")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = user_service.get_user_by_username(db, username)
    return user



@router.get("/{id}", response_model=UserRead, summary="Get a user by ID")
def get_user(id: int, db: Session = Depends(get_db)):
    return user_service.get_user(db, id)


@router.put("/{id}", response_model=UserRead, summary="Update a user")
def update_user(id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, id, data)


@router.delete("/{id}", summary="Delete a user")
def delete_user(id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, id)
    return {"detail": "User deleted"}