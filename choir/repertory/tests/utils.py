# -*- coding: utf-8 -*-

from django.test import TestCase
from choir.repertory.models import Song
from choir.repertory.utils import generate_chords_file, get_chords
from choir.repertory.utils import translate_chords

__all__ = [
    'UtilsTest',
    'TranslateChordsTest',
]


class UtilsTest(TestCase):
    fixtures = ['repertory_test.json']

    def test_generate_chords_file(self):
        return
        song = Song.objects.get(name='Everybody Hurts')
        generate_chords_file(song)

    def test_get_chords_only_title(self):
        song = Song(name='Let it be', chords='A B C')
        chords = get_chords(song)
        self.assertTrue('{title: Let it be}' in chords)
        self.assertFalse('{subtitle' in chords)

    def test_get_chords_subtitle(self):
        song = Song(name='Let it be', chords='A B C', tempo=85)
        chords = get_chords(song)
        self.assertTrue('{title: Let it be}' in chords)
        self.assertTrue('{subtitle: Tempo: 85}' in chords)

    def test_translate_chords(self):
        chords = ''
        self.assertEqual(translate_chords(chords), '')


class TranslateChordsTest(TestCase):
    def test_empty(self):
        self.assertEqual(translate_chords(''), '')

    def test_no_chords(self):
        self.assertEqual(translate_chords('Goofy\nYup'), 'Goofy\nYup')

    def test_chords(self):
        chords = '[D]When your day is [G]long and the [D]night'
        chords = translate_chords(chords)
        self.assertEqual(chords, '[Re]When your day is [Sol]long and the [Re]night')

    def test_altration(self):
        chords = '[Ab7]you\'re [D4]al---[B#m7]one'
        chords = translate_chords(chords)
        self.assertEqual(chords, '[Lab7]you\'re [Re4]al---[Si#m7]one')

    def test_double_chords(self):
        chords = u'[Dm]Are [D/F#]you'
        chords = translate_chords(chords)
        self.assertEqual(chords, '[Rem]Are [Re/Fa#]you')

    def test_unicode(self):
        chords = u'{title: àèìòùẻ l’a}[Ab7]Yooo'
        chords = translate_chords(chords)
        self.assertEqual(chords, "{title: a'e'i'o'u'e' l'a}[Lab7]Yooo")
        self.assertEqual(type(chords), str)
