from django.test import TestCase
from choir.repertory.models import Song, SongFile
from choir.repertory.models import get_song_file_name

__all__ = [
    'SongModelTest',
    'SongFileModelTest',
]


class SongModelTest(TestCase):
    fixtures = ['repertory_test.json']

    def setUp(self):
        self.song = Song.objects.get(pk=1)

    def test_get_score_display_empty(self):
        song = Song(name='Let it be')
        self.assertEqual(song.get_score_display(), '')

    def test_get_score_display_score_number(self):
        song = Song(name='Let it be', score_number=34)
        self.assertEqual(song.get_score_display(), '34')

    def test_get_score_display_score(self):
        self.song.score_number = None
        self.song.save()
        SongFile.objects.create(song=self.song, type='score')
        text = self.song.get_score_display()
        self.assertTrue('title="Kyrie eleison (Score)" data-content="Format: "><i class="icon-book"></i></a>' in text)

    def test_get_score_display_score_and_number(self):
        SongFile.objects.create(song=self.song, type='score')
        text = self.song.get_score_display()
        self.assertTrue('>21</a>' in text)

    def test_get_chords_url(self):
        self.song.chords = 'chords'
        self.song.save()
        url = self.song.get_chords_url()
        self.assertEqual(url, '/media/songfile/kyrie-eleison-chords.pdf')

    def test_get_chords_link(self):
        self.song.chords = 'chords'
        self.song.save()
        link = self.song.get_chords_link()
        self.assertEqual(link,
            '<a href="/media/songfile/kyrie-eleison-chords.pdf" '
            'title="Kyrie eleison (Accordi)" data-content="Format: pdf">'
            '<i class="icon-book"></i></a>')

    def test_get_chords_link_empty(self):
        link = self.song.get_chords_link()
        self.assertEqual(link, '')


class SongFileModelTest(TestCase):
    fixtures = ['repertory_test.json']

    def setUp(self):
        self.song = Song.objects.get(pk=1)

    def test_get_song_file_name_soprani(self):
        songfile = SongFile.objects.get(type='soprano')
        filename = get_song_file_name(songfile, 'a12.mp3')
        self.assertEqual(filename, 'songfile/kyrie-eleison-soprano.mp3')

    def test_get_song_file_name_bassi(self):
        songfile = SongFile.objects.get(type='basso')
        filename = get_song_file_name(songfile, 'a12.wav')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.wav')

    def test_get_song_file_name_midi(self):
        songfile = SongFile.objects.get(type='basso')
        filename = get_song_file_name(songfile, 'kyrie.MIDI')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.mid')

    def test_get_song_file_name_score_pdf(self):
        songfile = SongFile(song=self.song, type='score')
        filename = get_song_file_name(songfile, 'kr.PDF')
        self.assertEqual(filename, 'songfile/kyrie-eleison.pdf')

    def test_get_song_file_name_midi_complete(self):
        songfile = SongFile(song=self.song, type='midi')
        filename = get_song_file_name(songfile, 'kr.Mid')
        self.assertEqual(filename, 'songfile/kyrie-eleison.mid')
