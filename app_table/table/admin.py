from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'date',
                    'name',
                    'quantity',
                    'distance'
                    )
    list_editable = ('name',)
    search_fields = ('distance',)
    list_filter = ('quantity',)
    empty_value_display = '-пусто-'

admin.site.register(Record, RecordAdmin)