from bson import ObjectId
from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.models.products import Product


def get_collection_products(request: Request):
  return request.app.database["Products"]

def list_all_products(request):
   products = list(get_collection_products(request).find(limit=10))
   return products

def create_new_product(request: Request, product: Product):
    product = jsonable_encoder(product)
    new_product = get_collection_products(request).insert_one(product)
    created_product = get_collection_products(request).find_one({"_id": new_product.inserted_id})
    return created_product

def update_product(request: Request, id: str, product: Product):
    updated_product_data = {k: v for k, v in product.dict().items() if v is not None}
    if 'available_quantity' in updated_product_data:
        updated_product_data['available_quantity'] = int(updated_product_data['available_quantity'])  # Ensure it's converted to int
    update_result = get_collection_products(request).update_one(
        {"_id": ObjectId(id)},
        {"$set": updated_product_data}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found!")
    updated_product = get_collection_products(request).find_one({"_id": ObjectId(id)})
    return updated_product


        