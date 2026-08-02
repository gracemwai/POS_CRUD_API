from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.sale import SaleCreate, SaleUpdate, SaleRead
from pos.services import sale as sale_service

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=SaleRead, summary="Create a new sale")
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):
    return sale_service.create_sale(db, data)


@router.get("/", response_model=list[SaleRead], summary="List all sales")
def list_sales(db: Session = Depends(get_db)):
    return sale_service.list_sales(db)


@router.get("/{id}", response_model=SaleRead, summary="Get a sale by ID")
def get_sale(id: int, db: Session = Depends(get_db)):
    return sale_service.get_sale(db, id)


@router.put("/{id}", response_model=SaleRead, summary="Update a sale")
def update_sale(id: int, data: SaleUpdate, db: Session = Depends(get_db)):
    return sale_service.update_sale(db, id, data)


@router.delete("/{id}", summary="Delete a sale")
def delete_sale(id: int, db: Session = Depends(get_db)):
    sale_service.delete_sale(db, id)
    return {"detail": "Sale deleted"}