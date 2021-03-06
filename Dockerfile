FROM alpine:3.13

# Packages
RUN apk add --no-cache su-exec python3 nginx py3-pip uwsgi-python3 py3-psycopg2 tzdata gettext

# Requirements
COPY requirements /src/requirements
RUN    pip3 install -r /src/requirements/common.txt \
    && pip3 install -r /src/requirements/test.txt

ENV DJANGO_SETTINGS_MODULE=settings.docker

# Source
COPY . /src
RUN    chmod 755 /src/manage.py \
    && chmod 755 /src/docker/entrypoint.sh \
    && /src/manage.py collectstatic --link --noinput --verbosity=0 \
    && /src/manage.py compilemessages --verbosity=0

WORKDIR /src/
VOLUME ["/var/lib/nginx/tmp"]

EXPOSE 8000

ENTRYPOINT ["/src/docker/entrypoint.sh"]
CMD ["uwsgi", "--plugins", "/usr/lib/uwsgi/python3_plugin.so", "--master", "--processes", "1", "--threads", "8", "--chdir", "/src", "--wsgi", "settings.wsgi", "--http-socket", ":8000", "--stats", ":9191"]
