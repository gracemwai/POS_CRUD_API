# POS System API

A REST API for a Point of Sale (POS) system, built with FastAPI, SQLAlchemy, and PostgreSQL.
The API supports full CRUD operations for managing products, categories, customers, users, suppliers, sales, sale items, payments, and receipts, following a layered architecture (models, schemas, repositories, services, routers) with foreign key relationships enforced at the database level (e.g. a customer can place many sales, a sale can contain many sale items, and each sale generates exactly one receipt).
Interactive API documentation is available via Swagger UI once the server is running.
