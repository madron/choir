#!/bin/sh
set -e

coverage run --concurrency=multiprocessing manage.py test --parallel 1
coverage combine
coverage html
coverage report --skip-covered
