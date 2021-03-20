from django.conf import settings
from django.contrib.admin import site

# Member
if 'choir.member' in settings.INSTALLED_APPS:
    from choir.member import admin as member_admin
    from choir.member import models as member_models
    site.register(member_models.Role, member_admin.RoleAdmin)
    site.register(member_models.Member, member_admin.MemberAdmin)

# Repertory
if 'choir.repertory' in settings.INSTALLED_APPS:
    from choir.repertory import admin as repertory_admin
    from choir.repertory import models as repertory_models
    site.register(repertory_models.Period, repertory_admin.PeriodAdmin)
    site.register(repertory_models.Usage, repertory_admin.UsageAdmin)
    site.register(repertory_models.Song, repertory_admin.SongAdmin)

# Recording
if 'choir.recording' in settings.INSTALLED_APPS:
    from choir.recording import admin as recording_admin
    from choir.recording import models as recording_models
    site.register(recording_models.RecordingSong, recording_admin.RecordingSongAdmin)

# Events
if 'choir.events' in settings.INSTALLED_APPS:
    from choir.events import admin as events_admin
    from choir.events import models as events_models
    site.register(events_models.Event, events_admin.EventAdmin)

# Django user accounts
if 'account' in settings.INSTALLED_APPS:
    from account import models as account_models
    site.register(account_models.SignupCodeResult)
    site.register(account_models.EmailAddress)
    site.register(account_models.EmailConfirmation)
