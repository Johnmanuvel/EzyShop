## FastAPI and MongoDB 
A simple starter for building RESTful APIs with FastAPI and MongoDB. 

## Features

+ Python FastAPI backend.
+ MongoDB database.


## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console

pip install virtualenv

```

2. Install the modules listed in the `requirements.txt` file:

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **uvicorn**: A fast ASGI server for running web applications.
- **PyMongo**: The official MongoDB driver for Python.

```console

pip install -r requirements.txt

```

3. You also need to start your mongodb instance either locally, Create a `.env.dev` file. See the `.env.sample` for configurations. 

4. Start the application:

```console

 uvicorn main:app --reload

```

   The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080). 

5. Hit the address/docs to Use the Swagger interface to explore the available API endpoints, make requests, and test the functionality of the API.

## Endpoints

   Create a new product:
   Endpoint: POST /products
   Description: Creates a new product.

   Get all products:
   Endpoint: GET /products
   Description: Retrieves a list of all products.

   Create a new order:
   Endpoint: POST /orders
   Description: Creates a new order.

   Get all orders:
   Endpoint: GET /orders
   Description: Retrieves a list of all orders with optional pagination parameters (limit and offset).

   Find order by ID:
   Endpoint: GET /orders/{id}
   Description: Retrieves an order by its unique ID.

   Update a product:
   Endpoint: PUT /products/{id}
   Description: Updates an existing product by its unique ID.


