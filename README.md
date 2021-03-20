# Choir

## Tests

### Coverage
coverage run manage.py test && coverage report --skip-covered
coverage html

### Docker
docker-compose build && docker-compose -f docker-compose.test.yml run --rm sut
