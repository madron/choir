import factory
from django.core.files.uploadedfile import SimpleUploadedFile
from .. import models


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Event

    name = factory.Sequence(lambda n: 'event%s' % n)


class EventSongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.EventSong

    event = factory.SubFactory(EventFactory)
