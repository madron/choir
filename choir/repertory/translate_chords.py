#!/usr/bin/env python
# chordii -d | ./translate_chords.py > /etc/chordii.rc

import sys

TRANSLATIONS = [
    ('{define A', '{define La'),
    ('{define B', '{define Si'),
    ('{define D', '{define Re'),
    ('{define E', '{define Mi'),
    ('{define G', '{define Sol'),
    ('{define C', '{define Do'),
    ('{define F', '{define Fa'),
]


if __name__ == '__main__':
    lines = []
    text = sys.stdin.read()
    for k, v in TRANSLATIONS:
        text = text.replace(k, v)
    print text
