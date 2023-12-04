# Cook FastAPI

Copy & paste boilerplate for FastAPI projects.

I don't like tools like cookiecutter because they are adding their own boilerplate.
Copypasting FTW.

## Extras

### Postgres

`run.sh`

```bash
while ! nc -z postgres 5432; do
    sleep 1
done
```

`ci.yml`

```yaml
env:
    DATABASE_URL: postgresql+asyncpg://postgres:postgres@localhost:5432/test
services:
    postgres:
    image: postgres
    env:
        POSTGRES_DB: test
        POSTGRES_USER: postgres
        POSTGRES_PASSWORD: postgres
    ports:
        - 5432:5432
    options: --health-cmd pg_isready --health-interval 10s --health-timeout 5s --health-retries 5
```

`create_test_db.sh`

```bash
#!/bin/bash

psql -U postgres
psql -c "CREATE DATABASE test"
```

`docker-compose.yaml`

```yaml
services:
  postgres:
    image: "postgres:16-alpine"
    restart: on-failure
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U postgres" ]
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./devops/docker/create_test_db.sh:/docker-entrypoint-initdb.d/create_test_db.sh
    environment:
      - POSTGRES_DB=cook
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    ports:
      - "5432:5432"

volumes:
  postgres_data: {}
```

### DataDog

```bash
COMMAND=($(which ddtrace-run)" "$(which gunicorn)" "-k" "uvicorn.workers.UvicornWorker" "--preload" "--reuse-port" "--chdir=/app" "-b 0.0.0.0:${PORT:-8080}" "--max-requests=10000" "--max-requests-jitter=500" "-t" "60" "--graceful-timeout=30" "--keep-alive=2" "cook.main:app")
```
