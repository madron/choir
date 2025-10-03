### Builder
FROM python:3.13.7-alpine3.22 AS builder

RUN apk add --no-cache  poetry gcc python3-dev musl-dev linux-headers git
WORKDIR /src
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
RUN touch README.md
COPY pyproject.toml poetry.lock /src/
RUN poetry env use python3.13
RUN poetry install


### Image
FROM python:3.13.7-alpine3.22

# Packages
RUN apk add --no-cache gettext su-exec caddy

# Environment variables
ENV PATH="/src/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    TZ=Europe/Rome \
    DJANGO_SETTINGS_MODULE=settings.docker

# Source
COPY . /src
COPY --from=builder /src/.venv /src/.venv
RUN    chmod 755 /src/manage.py \
    && chmod 755 /src/docker/entrypoint.sh \
    && sync \
    && /src/manage.py collectstatic --link --noinput --verbosity=0 \
    && /src/manage.py compilemessages --verbosity=0

WORKDIR /src/
VOLUME ["/var/lib/caddy/tmp"]

EXPOSE 8000

ENTRYPOINT ["/src/docker/entrypoint.sh"]
CMD ["uwsgi", "--master", "--processes", "4", "--threads", "8", "--chdir", "/src", "--wsgi", "settings.wsgi", "--http-socket", ":8000", "--stats", ":9191"]
