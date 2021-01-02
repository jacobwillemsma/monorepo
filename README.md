# monorepo
A nice starting point for Postgres/FastAPI/SQLAlchemy/Alembic/React

# Building
Run `./scripts/build.sh` and let Docker handle the rest.

# Usage
Your database will be on `localhost:5432`, you can connect with `PGPASSWORD=password psql -h localhost -U postgres -p 5432 -d postgres`

Your React frontend will be on `localhost:80` or just `localhost`

Your Backend will be on `localhost:902`
