from django.contrib import admin

from news.models import Articles
from mainApp.models import Area, Service


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'time', 'price', 'area')
    list_filter = ('price', 'area')
    pass


admin.site.register(Articles)
#admin.site.register(Area, AreaAdmin)
#admin.site.register(Service, ServiceAdmin)

