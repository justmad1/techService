from django.contrib import admin

from news.models import Articles
from master_office.models import Master,Order, OrderLine, Comment
from mainApp.models import Area, Service

admin.autodiscover()

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'time', 'price', 'area')
    list_filter = ('price', 'area')
    pass


admin.site.register(Articles)
admin.site.register(Master)
admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Comment)
#admin.site.register(Area, AreaAdmin)
#admin.site.register(Service, ServiceAdmin)

