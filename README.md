# Choir

## Tests

### Coverage
coverage run manage.py test && coverage report --skip-covered
coverage html

### Docker
docker-compose build && docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm django /src/docker/coverage.sh
