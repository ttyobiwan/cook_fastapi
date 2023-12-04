FROM python:3.11.4-slim-buster as base

EXPOSE 8080

WORKDIR /code

# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/code"

# Install necessary soft
RUN apt-get update \
    && apt-get install -y netcat curl git make gcc python3-dev libpq-dev \
    && apt-get clean

# Dev environment
FROM base as dev

ENV DEVELOPMENT=1 \
    DEBUG=1

# Copy & install dependencies
COPY ./requirements ./requirements
RUN pip install -r ./requirements/dev.txt

COPY . .

CMD ["bash", "scripts/run.sh"]

# Production environment
FROM base as prod

RUN useradd -mr nonroot

USER nonroot

ENV PATH=$PATH:/home/nonroot/.local/bin

COPY --chown=nonroot:nonroot ./requirements ./requirements
RUN pip install -r ./requirements/base.txt

COPY --chown=nonroot:nonroot . /code

CMD ["bash", "scripts/run.sh"]
