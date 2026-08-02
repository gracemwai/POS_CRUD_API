from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from pos.services import category as category_service

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=CategoryRead, summary="Create a new category")
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category(db, data)


@router.get("/", response_model=list[CategoryRead], summary="List all categories")
def list_categories(db: Session = Depends(get_db)):
    return category_service.list_categories(db)


@router.get("/{id}", response_model=CategoryRead, summary="Get a category by ID")
def get_category(id: int, db: Session = Depends(get_db)):
    return category_service.get_category(db, id)


@router.put("/{id}", response_model=CategoryRead, summary="Update a category")
def update_category(id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return category_service.update_category(db, id, data)


@router.delete("/{id}", summary="Delete a category")
def delete_category(id: int, db: Session = Depends(get_db)):
    category_service.delete_category(db, id)
    return {"detail": "Category deleted"}