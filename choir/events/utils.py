from django.utils.translation import ugettext as _
import xlwt


def get_event_xls(event):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet(_('Songs'))
    sheet.write(0, 1, _('page').capitalize())
    sheet.write(0, 3, _('score').capitalize())
    sheet.write(0, 4, _('soloist').capitalize())
    sheet.write(0, 5, _('guide').capitalize())
    row = 1
    for eventsong in event.eventsong_set.all():
        song = eventsong.song
        name = song.name
        if eventsong.note:
            name = '%s (%s)' % (name, eventsong.note)
        sheet.write(row, 0, str(eventsong.usage))
        sheet.write(row, 1, song.page)
        sheet.write(row, 2, name)
        sheet.write(row, 3, song.score_number)
        sheet.write(row, 4, eventsong.soloist)
        sheet.write(row, 5, eventsong.guide)
        row += 1
    return xls
