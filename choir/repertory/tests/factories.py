import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from .. import models


class PeriodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Period

    name = factory.Sequence(lambda n: 'period%s' % n)


class UsageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Usage

    name = factory.Sequence(lambda n: 'usage%s' % n)


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
