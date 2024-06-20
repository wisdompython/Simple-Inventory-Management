# Online Store Inventory and Supplier Management API

## Setup Instructions

1. Clone the repository
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```
    python manage.py migrate
    ```
4. Generate Swagger UI schema:
    ```
    python manage.py spectacular --file schema.yml

    ```
4. Run the development server:
    runs on localhost and port 8000 by default
    ```
    python manage.py runserver
    ```

## API Endpoints

### Inventory Items

- **GET /inventory_items/**: List all inventory items
- **POST /inventory_items/**: Create a new inventory item
- **GET /inventory_items/{id}/**: Retrieve a specific inventory item
- **PUT /inventory_items/{id}/**: Update a specific inventory item
- **DELETE /inventory_items/{id}/**: Delete a specific inventory item

### Suppliers

- **GET /suppliers/**: List all suppliers
- **POST /suppliers/**: Create a new supplier
- **GET /suppliers/{id}/**: Retrieve a specific supplier
- **PUT /suppliers/{id}/**: Update a specific supplier
- **DELETE /suppliers/{id}/**: Delete a specific supplier

### swagger docs url

- **swagger-ui : /api/schema/swagger-ui/**
- **redoc : /api/schema/redoc**

### postman docs links
Find Here : [Postman Docs](https://www.postman.com/galactic-comet-374170/workspace/priority-soft-django-code-test/collection/21778720-e42218c3-0699-4057-b4ec-af7a2b7c45f4?action=share&creator=21778720)