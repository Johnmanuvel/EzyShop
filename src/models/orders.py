from pydantic import BaseModel, Field
import uuid
import datetime


class Items(BaseModel):
    productId:str
    boughtQuantity:int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "productId": "1234",
                "boughtQuantity": 5,
            }
        }

class Address(BaseModel):
    city:str
    country:str
    zip:int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "city": "NY",
                "country": "America",
                "zip": 100012
            }
        }

class Order(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    timestamp: datetime.datetime = datetime.datetime.now()
    items : list[Items]
    total_amount:int
    address:list[Address]

    
