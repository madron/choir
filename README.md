# Choir

## Tests

### Coverage
coverage run manage.py test && coverage report --skip-covered
coverage html

### Docker
docker-compose build && docker-compose -f docker-compose.test.yml run --rm sut

## Translation

### Make messages
```
cd choir/player && django-admin makemessages --all && cd ../..
cd choir/events && django-admin makemessages --all && cd ../..
cd choir/repertory && django-admin makemessages --all && cd ../..
```

### Compile messages
```
./manage.py compilemessages
```

## Tag version to trigger github build
```
export TAG=v1.1.xxx
git tag -a $TAG -m "Release $TAG"
git push origin $TAG
```