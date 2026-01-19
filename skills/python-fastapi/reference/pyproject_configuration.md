# Pyproject example

```toml
# pyproject.toml
[project]
name = "my-fastapi-project"
version = "1.0.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.111.0",
    "pydantic>=2.7.0",
    "sqlalchemy[asyncio]>=2.0.30",
    "alembic>=1.13.0",
    "asyncpg>=0.29.0",
]

[dependency-groups]
dev = [
    "mypy>=1.19.0",
    "pytest>=9.0.2",
    "pytest-asyncio>=1.3.0"
    "ruff>=0.14.10",
    "httpx>=0.28.1",
]
```