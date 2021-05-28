from django.contrib import admin
from .models import TimeUUID
# Register your models here.


class TimeUUIDAdmin(admin.ModelAdmin):
    list_display= ('time_date','uuid_value',)


admin.site.register(TimeUUID, TimeUUIDAdmin)
