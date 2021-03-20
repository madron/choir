# -*- coding: utf-8 -*-

import os
import re
from os import remove
from os.path import join
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from time import sleep
from django.conf import settings

CHORDS_DIR = join(settings.MEDIA_ROOT, 'songfile')
NOTES = {
    'C': 'Do',
    'D': 'Re',
    'E': 'Mi',
    'F': 'Fa',
    'G': 'Sol',
    'A': 'La',
    'B': 'Si',
}
CHAR_REPLACE = {
    u'à': "a'",
    u'è': "e'",
    u'ẻ': "e'",
    u'ì': "i'",
    u'ò': "o'",
    u'ù': "u'",
    u'’': "'",
}
for key, value in NOTES.iteritems():
    CHAR_REPLACE['[%s' % key] = '[%s' % value
    CHAR_REPLACE['/%s' % key] = '/%s' % value
re_translation = re.compile(u'\[A|\[B|\[C|\[D|\[E|\[F|\[G|/A|/B|/C|/D|/E|/F|\[G|à|è|ẻ|ì|ò|ù|’')


def generate_chords_file(song):
    chords = translate_chords(get_chords(song))
    filename = join(settings.MEDIA_ROOT, 'songfile',
        '%s-chords.pdf' % song.slug)
    # Write chords on filesystem
    generate_chords_pdf(chords, filename=filename)


def generate_chords_pdf(chords, filename=None):
    # Write chords on filesystem
    chords_file = NamedTemporaryFile(delete=False)
    chords_file.write(chords)
    chords_file.close()
    # Write pdf file in CHORDS_DIR
    if filename:
        file_name = filename
    else:
        pdf_file = NamedTemporaryFile()
        pdf_file.close()
        file_name = pdf_file.name
    try:
        env = os.environ.copy()
        env['CHORDIIRC'] = '/etc/chordii.rc'
        parameters = ''
        cmd = ['chordii %s %s | ps2pdf - %s' % (parameters, chords_file.name,
            file_name)]
        command = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, env=env)
        sleep(0.1)
    finally:
        remove(chords_file.name)
    stderr = command.stderr.read().strip()
    if filename:
        return stderr
    else:
        pdf_file = open(file_name, 'r')
        pdf = pdf_file.read()
        pdf.close()
        return stderr, pdf


def get_chords(song):
    chords = song.chords
    # Add header rows
    headers = [
        '{title: %s}' % song.name,
    ]
    infos = []
    if song.number:
        infos.append('N. %s' % song.number)
    if song.page:
        infos.append('Pag. %d' % song.page)
    if song.score_number:
        infos.append('Part. %d' % song.score_number)
    if song.tempo:
        infos.append('Tempo: %d' % song.tempo)
    if infos:
        headers.append('{subtitle: %s}' % ' - '.join(infos))
    return '%s\n\n%s' % ('\n'.join(headers), chords)


def translate_chords(chords):
    def translate(match):
        return CHAR_REPLACE[match.group(0)]
    text = re_translation.sub(translate, chords)
    return str(text.encode('ascii'))
