# Choir

## Tests

### Coverage
coverage run manage.py test && coverage report --skip-covered
coverage html

### Docker
docker-compose build && docker-compose -f docker-compose.test.yml run --rm sut

## Tag version to trigger github build
```
export TAG=v1.1.xxx
git tag -a $TAG -m "Release $TAG"
git push origin $TAG
```