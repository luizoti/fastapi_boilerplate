# Alembic

docs: https://alembic.sqlalchemy.org/en/latest/tutorial.html

Create migration:

```bash
  alembic revision -m "create account table"
```

Run migrate:

```bash
  alembic upgrade head
```
