from fastapi import APIRouter, Request, status, Query
from src.models.products import Product
from src.models.orders import Order
import src.rules.products as product
import src.rules.orders as orders 


router = APIRouter(tags=["Products & Orders"])

@router.post("/products", response_description="Create new product", status_code=status.HTTP_201_CREATED, response_model=Product)
def create_product(request: Request, products: Product):
    return product.create_new_product(request, products)

@router.get("/products", response_description="Get all products", status_code=status.HTTP_200_OK, response_model=list[Product])
def list_all_products(request: Request):
    return product.list_all_products(request)

@router.post("/orders", response_description="Create new order", status_code=status.HTTP_201_CREATED, response_model=Order)
def create_order(request: Request, order: Order):
    return orders.create_new_order(request, order)

@router.get("/orders", response_description="Get all orders", status_code=status.HTTP_200_OK, response_model=list[Order])
def list_all_orders(request: Request, limit: int = Query(10, le=100), offset: int = Query(0, ge=0)):
    return orders.list_orders(request, limit, offset)

@router.get("/orders/{id}", response_description="Find order by id", status_code=status.HTTP_200_OK, response_model=Order)
def find_order(request: Request, id:str):
    return orders.find_order(request,id)

@router.put("/products/{id}", response_description="Update product", status_code=status.HTTP_200_OK, response_model=Product)
def update_product_endpoint(request: Request, id: str, products: Product):
    return product.update_product(request, id, products)