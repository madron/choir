import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'test%s' % n)
    # password: pass
    password = 'pbkdf2_sha256$12000$GMh486z94kmq$yaxEmZjcLvlnBoKWNG2Y926givWTo739b6tqWnw8eBM='
    is_staff = True
    is_superuser = True
    email = 'test@example.com'
