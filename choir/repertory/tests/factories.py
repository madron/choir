import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from .. import models


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Song

    name = factory.Sequence(lambda n: 'song%s' % n)
    slug = factory.Sequence(lambda n: 'slug%s' % n)


class SongFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SongFile

    song = factory.SubFactory(SongFactory)
    file = SimpleUploadedFile('file.pdf', '')
