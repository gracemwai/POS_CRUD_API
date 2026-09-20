from fastapi import FastAPI
from database import Base, engine
import pos.models as models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="POS API", version="1.0.0")

from pos.routers import (
    category_router, 
    customer_router,
    product_router, 
    user_router,
    supplier_router, 
    sale_router, 
    sale_item_router, 
    payment_router, 
    receipt_router,  
)




app.include_router(category_router)
app.include_router(customer_router)
app.include_router(product_router)
app.include_router(user_router)
app.include_router(supplier_router)
app.include_router(sale_router)
app.include_router(sale_item_router)
app.include_router(payment_router)
app.include_router(receipt_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Point of Sale System API"}

