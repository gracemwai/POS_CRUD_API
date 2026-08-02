from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.receipt import ReceiptCreate, ReceiptUpdate, ReceiptRead
from pos.services import receipt as receipt_service

router = APIRouter(prefix="/receipts", tags=["Receipts"])


@router.post("/", response_model=ReceiptRead, summary="Create a new receipt")
def create_receipt(data: ReceiptCreate, db: Session = Depends(get_db)):
    return receipt_service.create_receipt(db, data)


@router.get("/", response_model=list[ReceiptRead], summary="List all receipts")
def list_receipts(db: Session = Depends(get_db)):
    return receipt_service.list_receipts(db)


@router.get("/{id}", response_model=ReceiptRead, summary="Get a receipt by ID")
def get_receipt(id: int, db: Session = Depends(get_db)):
    return receipt_service.get_receipt(db, id)


@router.put("/{id}", response_model=ReceiptRead, summary="Update a receipt")
def update_receipt(id: int, data: ReceiptUpdate, db: Session = Depends(get_db)):
    return receipt_service.update_receipt(db, id, data)


@router.delete("/{id}", summary="Delete a receipt")
def delete_receipt(id: int, db: Session = Depends(get_db)):
    receipt_service.delete_receipt(db, id)
    return {"detail": "Receipt deleted"}