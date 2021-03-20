#!/bin/bash
set -e

if [ "$1" = 'uwsgi' ]; then
    chown -R uwsgi:uwsgi /media
    until gosu uwsgi /src/manage.py syncdb --noinput; do
        echo "$(date) - waiting for db..."
        sleep 1
    done
    gosu uwsgi /src/manage.py migrate --noinput
    exec gosu uwsgi "$@"
elif [ "$1" = 'nginx' ]; then
    exec nginx "-g daemon off;"
else
    exec "$@"
fi
