from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.payment import PaymentCreate, PaymentUpdate, PaymentRead
from pos.services import payment as payment_service

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", response_model=PaymentRead, summary="Create a new payment")
def create_payment(data: PaymentCreate, db: Session = Depends(get_db)):
    return payment_service.create_payment(db, data)


@router.get("/", response_model=list[PaymentRead], summary="List all payments")
def list_payments(db: Session = Depends(get_db)):
    return payment_service.list_payments(db)


@router.get("/{id}", response_model=PaymentRead, summary="Get a payment by ID")
def get_payment(id: int, db: Session = Depends(get_db)):
    return payment_service.get_payment(db, id)


@router.put("/{id}", response_model=PaymentRead, summary="Update a payment")
def update_payment(id: int, data: PaymentUpdate, db: Session = Depends(get_db)):
    return payment_service.update_payment(db, id, data)


@router.delete("/{id}", summary="Delete a payment")
def delete_payment(id: int, db: Session = Depends(get_db)):
    payment_service.delete_payment(db, id)
    return {"detail": "Payment deleted"}