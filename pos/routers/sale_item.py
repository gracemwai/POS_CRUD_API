from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.sale_item import SaleItemCreate, SaleItemUpdate, SaleItemRead
from pos.services import sale_item as sale_item_service

router = APIRouter(prefix="/sale-items", tags=["Sale Items"])


@router.post("/", response_model=SaleItemRead, summary="Create a new sale item")
def create_sale_item(data: SaleItemCreate, db: Session = Depends(get_db)):
    return sale_item_service.create_sale_item(db, data)


@router.get("/", response_model=list[SaleItemRead], summary="List all sale items")
def list_sale_items(db: Session = Depends(get_db)):
    return sale_item_service.list_sale_items(db)


@router.get("/{id}", response_model=SaleItemRead, summary="Get a sale item by ID")
def get_sale_item(id: int, db: Session = Depends(get_db)):
    return sale_item_service.get_sale_item(db, id)


@router.put("/{id}", response_model=SaleItemRead, summary="Update a sale item")
def update_sale_item(id: int, data: SaleItemUpdate, db: Session = Depends(get_db)):
    return sale_item_service.update_sale_item(db, id, data)


@router.delete("/{id}", summary="Delete a sale item")
def delete_sale_item(id: int, db: Session = Depends(get_db)):
    sale_item_service.delete_sale_item(db, id)
    return {"detail": "Sale item deleted"}