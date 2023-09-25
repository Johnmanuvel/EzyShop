from pydantic import BaseModel, Field
import uuid

class Product(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    product_name: str 
    product_price: int
    available_quantity: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "product_name": "TV",
                "product_price": 15000,
                "available_quantity": 5
            }
        }



    
