from bson import ObjectId
from fastapi import Request, HTTPException, status, Query
from fastapi.encoders import jsonable_encoder
from src.models.orders import Order


def get_collection_order(request: Request):
  return request.app.database["Orders"]

def create_new_order(request: Request, order: Order):
    order = jsonable_encoder(order)
    new_order = get_collection_order(request).insert_one(order)
    created_order = get_collection_order(request).find_one({"_id": new_order.inserted_id})
    return created_order

def list_orders(request: Request, limit: int = Query(10, le=100), offset: int = Query(0, ge=0)):
    orders = list(get_collection_order(request).find().skip(offset).limit(limit))
    return orders

def find_order(request,id):
    if (order := get_collection_order(request).find_one({"_id": ObjectId(id)})):
        return order
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order with id {id} not found!")


        