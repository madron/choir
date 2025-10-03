#!/bin/sh
set -e

if [ "$1" = 'uwsgi' ]; then
    echo 'Wait for database'
    su-exec uwsgi python3 /src/manage.py wait_for_database
    echo 'Migrate'
    su-exec uwsgi python3 /src/manage.py migrate --noinput
    echo 'Admin user'
    su-exec uwsgi python3 /src/manage.py create_default_admin
    echo su-exec nobody $*
    exec su-exec nobody $*
elif [ "$1" = 'caddy' ]; then
    su-exec nobody caddy run --config /src/docker/Caddyfile --watch
else
    exec "$@"
fi
