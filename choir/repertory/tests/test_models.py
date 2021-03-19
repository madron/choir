from django.test import SimpleTestCase, TestCase
from choir.repertory import models
from . import factories


class SongModelTest(SimpleTestCase):
    def test_str(self):
        song = models.Song(name='Let it be')
        self.assertEqual(str(song), 'Let it be')


class GetSongFileNameTest(TestCase):
    def test_get_song_file_name_soprani(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='soprano')
        filename = models.get_song_file_name(songfile, 'a12.mp3')
        self.assertEqual(filename, 'songfile/kyrie-eleison-soprano.mp3')

    def test_get_song_file_name_bassi(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='basso')
        filename = models.get_song_file_name(songfile, 'a12.wav')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.wav')

    def test_get_song_file_name_midi(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='basso')
        filename = models.get_song_file_name(songfile, 'kyrie.MIDI')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.mid')

    def test_get_song_file_name_score_pdf(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='score')
        filename = models.get_song_file_name(songfile, 'kr.PDF')
        self.assertEqual(filename, 'songfile/kyrie-eleison.pdf')

    def test_get_song_file_name_midi_complete(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='midi')
        filename = models.get_song_file_name(songfile, 'kr.Mid')
        self.assertEqual(filename, 'songfile/kyrie-eleison.mid')


class SongFileModelTest(SimpleTestCase):
    def test_str(self):
        obj = models.SongFile(type='soprano')
        self.assertEqual(str(obj), 'soprano')
