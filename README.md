backend/
│
├── database/
│   → Creates the database connection and SQLAlchemy session.
│   → (Not activating PostgreSQL; PostgreSQL is already running.)
│
├── models/
│   → Defines database tables using SQLAlchemy ORM classes.
│
├── schemas/
│   → Defines Pydantic models for request validation and response serialization.
│
├── routers/
│   → Defines API endpoints and receives client requests.
│
├── services/
│   → Contains business logic. Routers call services to perform application tasks.
│
├── utils/
│   → Contains reusable helper/utility functions used across the project.
│
└── main.py
    → Entry point of the FastAPI application.
    → Creates the FastAPI app, includes routers, and starts the application.





## Fast API
- for virtual enviroment: uv venv --python 3.10.0
- for installing FastAPI & uvicorn: uv pip install fastapi uvicorn
- for starting backend: uvicorn main:app --reload

# "FastAPI is built on top of Starlette and Pydantic."
- Starlette handles the speed: It provides the underlying async web routing, ensuring the framework is incredibly fast and efficient.(Aysnchronous)

- Pydantic handles the data: It ensures the incoming JSON data matches the exact structure and types (like int, str, bool) your Python code expects. If someone sends bad data, Pydantic automatically catches it and returns a clear error message.
    -- The Smart Fixes (Coercion): If a user sends "25" (text) for an int field, Pydantic says, "I can fix this," and turns it into the number 25.
    -- The Hard Blocks (Validation Error): If a user sends "twenty-five" or leaves the field completely blank, Pydantic stops the request immediately. It throws a 422 Unprocessable Entity error back to the user, explaining exactly what they got wrong so your Python code never has to deal with broken data.

# CRUD Operations Mapping

| Letter | Operation | Description | HTTP Method | FastAPI Example |
| :---: | :---       | :---             | :---:  | :---                                       |
| **C** | **Create** | Adding new data. | `POST` | `@app.post("/users")` (Sign up a new user) |
| **R** | **Read** | Fetching or viewing existing data. | `GET` | `@app.get("/users/{id}")` (View a user profile) |
| **U** | **Update** | Modifying existing data. | `PUT` / `PATCH` | `@app.put("/users/{id}")` (Change a password) |
| **D** | **Delete** | Removing data. | `DELETE` | `@app.delete("/users/{id}")` (Delete an account) |

# Important backend Codes
- 200 OK: Request succeeded (e.g., fetching a user profile).
- 201 Created: A new resource was successfully made (e.g., a new user signed up).
- 400 Bad Request: The request data was malformed or syntax was wrong.
- 401 Unauthorized: [Missing] The user is not logged in. (Crucial for security).
- 403 Forbidden: [Missing] The user is logged in, but doesn't have permission to see this (e.g., a regular user trying to access an Admin panel).
- 404 Not Found: The URL or resource does not exist.
- 422 Unprocessable Entity: [Missing] (Very important for FastAPI). This is the exact error Pydantic throws when JSON data types don't match your Python expectations.
