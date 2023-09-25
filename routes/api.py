from fastapi import APIRouter
from src.endpoints import productsAndOrders

router = APIRouter()
router.include_router(productsAndOrders.router)
