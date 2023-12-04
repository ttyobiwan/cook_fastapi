#!/bin/bash

set -exo pipefail

if [[ -z ${DEVELOPMENT} ]]; then
    COMMAND=("$(which gunicorn)" "-k" "uvicorn.workers.UvicornWorker" "--preload" "--reuse-port" "--chdir=/app" "-b 0.0.0.0:${PORT:-8080}" "--max-requests=10000" "--max-requests-jitter=500" "-t" "60" "--graceful-timeout=30" "--keep-alive=2" "cook.main:app")
else
    COMMAND=("$(which uvicorn)" "cook.main:app" "--reload" "--workers" "1" "--host" "0.0.0.0" "--port" "${PORT:-8080}" "--no-access-log")
fi

exec "${COMMAND[@]}"
