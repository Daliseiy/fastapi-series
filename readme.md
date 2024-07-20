# FastBlogger

FastBlogger is a project created for a YouTube tutorial to teach people FastAPI by building a blog application. This project demonstrates the use of FastAPI, SQLAlchemy, Docker, and other technologies.


## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- Docker Compose

### Setup

1. **Create and activate a virtual environment(Optional):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the necessary environment variables. You can use `.env.prod` for production.

### Running with Docker

1. **Build and run the Docker container:**

    ```bash
    docker-compose -f local.yml up --build
    ```

2. **Stop the Docker container:**

    ```bash
    docker-compose -f local.yml down
    ```

### Database Migration

Alembic is used for database migrations. Make sure to configure `alembic.ini` file properly.

1. **Initialize Alembic**

    ```bash
    alembic init alembic
    ```

2. **Create a new migration:**

    ```bash
    alembic revision --autogenerate -m "description"
    ```

2. **Apply migrations:**

    ```bash
    alembic upgrade head
    ```


## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.


## Links

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)

## Contact

For any inquiries, please contact me at [obakunleoluseye@gmail.com].

---

This project was created as part of a YouTube tutorial series. Check out the video [here](https://www.youtube.com/watch?v=OfSmvw2d3eU&list=PLF4NJty07PAVY1BSekofr2Kv9ZX6mauDw) for a step-by-step guide.
