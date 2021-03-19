from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create default admin user'
    requires_model_validation = False

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, action='store', dest='username', default='admin')
        parser.add_argument('--password', type=str, action='store', dest='password', default='admin')
        parser.add_argument('--email', type=str, action='store', dest='email', default='admin@example.com')

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.filter(username=options['username']).exists():
            self.stdout.write(self.style.SUCCESS("User '{}' already present.".format(options['username'])))
        else:
            User.objects.create_superuser(
                username=options['username'],
                email=options['email'],
                password=options['password'],
            )
            self.stdout.write(self.style.SUCCESS("User '{}' created.".format(options['username'])))
