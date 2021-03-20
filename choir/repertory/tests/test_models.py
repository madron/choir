from django.test import SimpleTestCase, TestCase
from choir.repertory import models
from . import factories


class SongModelTest(SimpleTestCase):
    def test_str(self):
        song = models.Song(name='Let it be')
        self.assertEqual(str(song), 'Let it be')


class GetSongFileNameTest(TestCase):
    def test_choir_midi(self):
        songfile = factories.SongFileFactory(song__slug='title', type='choir')
        filename = models.get_song_file_name(songfile, 'f.Mid')
        self.assertEqual(filename, 'songfile/title-choir.mid')

    def test_choir_mp3(self):
        songfile = factories.SongFileFactory(song__slug='title', type='choir')
        filename = models.get_song_file_name(songfile, 'f.mp3')
        self.assertEqual(filename, 'songfile/title-choir.mp3')

    def test_chords(self):
        songfile = factories.SongFileFactory(song__slug='title', type='chords')
        filename = models.get_song_file_name(songfile, 'f.pdf')
        self.assertEqual(filename, 'songfile/title-chords.pdf')

    def test_lyrics(self):
        songfile = factories.SongFileFactory(song__slug='title', type='lyrics')
        filename = models.get_song_file_name(songfile, 'f.pdf')
        self.assertEqual(filename, 'songfile/title-lyrics.pdf')

    def test_score_pdf(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='score')
        filename = models.get_song_file_name(songfile, 'kr.PDF')
        self.assertEqual(filename, 'songfile/kyrie-eleison-score.pdf')

    def test_midi(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='midi')
        filename = models.get_song_file_name(songfile, 'kr.Mid')
        self.assertEqual(filename, 'songfile/kyrie-eleison-midi.mid')

    def test_soprano(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='soprano')
        filename = models.get_song_file_name(songfile, 'a12.mp3')
        self.assertEqual(filename, 'songfile/kyrie-eleison-soprano.mp3')

    def test_basso(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='basso')
        filename = models.get_song_file_name(songfile, 'a12.wav')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.wav')

    def test_basso_midi(self):
        songfile = factories.SongFileFactory(song__slug='kyrie-eleison', type='basso')
        filename = models.get_song_file_name(songfile, 'kyrie.MIDI')
        self.assertEqual(filename, 'songfile/kyrie-eleison-basso.mid')


class SongFileModelTest(SimpleTestCase):
    def test_str(self):
        obj = models.SongFile(type='soprano')
        self.assertEqual(str(obj), 'soprano')
