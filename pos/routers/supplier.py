from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.supplier import SupplierCreate, SupplierUpdate, SupplierRead
from pos.services import supplier as supplier_service

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("/", response_model=SupplierRead, summary="Create a new supplier")
def create_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_service.create_supplier(db, data)


@router.get("/", response_model=list[SupplierRead], summary="List all suppliers")
def list_suppliers(db: Session = Depends(get_db)):
    return supplier_service.list_suppliers(db)


@router.get("/{id}", response_model=SupplierRead, summary="Get a supplier by ID")
def get_supplier(id: int, db: Session = Depends(get_db)):
    return supplier_service.get_supplier(db, id)


@router.put("/{id}", response_model=SupplierRead, summary="Update a supplier")
def update_supplier(id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    return supplier_service.update_supplier(db, id, data)


@router.delete("/{id}", summary="Delete a supplier")
def delete_supplier(id: int, db: Session = Depends(get_db)):
    supplier_service.delete_supplier(db, id)
    return {"detail": "Supplier deleted"}