from django import template
from choir.repertory.models import SongFile
from ..models import EventSong


register = template.Library()


@register.simple_tag(name="get_eventsong_section_songfile")
def get_eventsong_section_songfile(eventsong: EventSong, section: str) -> SongFile:
    songfiles = eventsong.song.songfile_set.filter(type=section)
    if songfiles:
        return songfiles[0]
    return None
