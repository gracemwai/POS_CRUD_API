from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from pos.schemas.customer import CustomerCreate, CustomerUpdate, CustomerRead
from pos.services import customer as customer_service

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerRead, summary="Create a new customer")
def create_customer(data: CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, data)


@router.get("/", response_model=list[CustomerRead], summary="List all customers")
def list_customers(db: Session = Depends(get_db)):
    return customer_service.list_customers(db)


@router.get("/{id}", response_model=CustomerRead, summary="Get a customer by ID")
def get_customer(id: int, db: Session = Depends(get_db)):
    return customer_service.get_customer(db, id)


@router.put("/{id}", response_model=CustomerRead, summary="Update a customer")
def update_customer(id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    return customer_service.update_customer(db, id, data)


@router.delete("/{id}", summary="Delete a customer")
def delete_customer(id: int, db: Session = Depends(get_db)):
    customer_service.delete_customer(db, id)
    return {"detail": "Customer deleted"}