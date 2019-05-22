from django.contrib import admin
from .models import Sensor, SensorHistory


class SensorAdmin(admin.ModelAdmin):
    pass

class SensorHistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sensor, SensorAdmin)

admin.site.register(SensorHistory, SensorHistoryAdmin)


# Register your models here.
