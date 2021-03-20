FROM madron/uwsgi
MAINTAINER Massimiliano Ravelli <massimiliano.ravelli@gmail.com>

# Packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y libpq-dev git \
    && rm -rf /var/lib/apt/lists/*

# Requirements
COPY requirements /src/requirements
RUN pip install -r /src/requirements/docker.txt

# Source
COPY . /src

# Nginx site
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# Settings
ENV DJANGO_SETTINGS_MODULE=settings.docker

# Static files
RUN /src/manage.py collectstatic --link --noinput --verbosity=0

VOLUME ["/run/uwsgi"]
VOLUME ["/sqlite"]

ENTRYPOINT ["/src/docker/entrypoint.sh"]
CMD ["uwsgi", "--master", "--processes", "1", "--threads", "1", "/src/docker/uwsgi.ini"]
