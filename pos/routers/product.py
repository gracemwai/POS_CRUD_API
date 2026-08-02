from fastapi import APIRouter, Depends, status
from database import get_db
from sqlalchemy.orm import Session
from pos.services import product
from pos.schemas.product import ProductCreate, ProductUpdate, ProductRead

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductRead])
def list_products(db: Session = Depends(get_db)):
    return product.list_products(db)


@router.get("/{id}", response_model=ProductRead)
def get_product(id: int, db: Session = Depends(get_db)):
    return product.get_product(db, id)


@router.post("/", response_model=ProductRead)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    return product.create_product(db, data)


@router.put("/{id}", response_model=ProductRead)
def update_product(id: int, data: ProductUpdate, db: Session = Depends(get_db)):
    return product.update_product(db, id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    product.delete_product(db, id)