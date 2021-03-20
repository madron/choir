from django.contrib import admin
from django.contrib.admin.util import unquote
from choir.recording import forms
from choir.recording import models


class RecordingSongPartInline(admin.TabularInline):
    model = models.RecordingSongPart
    form = forms.RecordingSongPartForm
    # readonly_fields = ['type']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class RecordingSongAdmin(admin.ModelAdmin):
    list_display = (
        'importance', 'song', 'music_status', 'soloist_status',
        'soprano_status', 'contralto_status', 'tenore_status', 'basso_status',
        'completed')
    list_display_links = ('song',)
    list_filter = ('completed',)
    list_editable = ('importance',)
    inlines = [RecordingSongPartInline]
    form = forms.RecordingSongForm

    class Media:
        # css = dict(all=['recording/css/status.css'])
        js = ['recording/js/status.js']

    def get_fieldsets(self, request, obj=None):
        fields = ['song']
        if obj:
            fields = [('importance', 'completed')]
        fieldsets = (
            (None, dict(
                fields=fields,
            )),
        )
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        fields = super(RecordingSongAdmin, self).get_readonly_fields(
            request, obj)
        if obj:
            return list(fields) + ['song']
        return fields

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, unquote(object_id))
        extra_context = extra_context or dict()
        extra_context['title'] = unicode(obj)
        return super(RecordingSongAdmin, self).change_view(request, object_id,
            form_url=form_url, extra_context=extra_context)
