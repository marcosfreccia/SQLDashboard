from django.contrib import admin
from server.models import Versions,Servers

# Register your models here.

admin.site.site_header = 'Administration'
admin.site.site_title = 'Admin'
admin.site.index_title = "SQL Dashboard"

class VersionsAdmin(admin.ModelAdmin):
    list_display = ["name","is_active"]
    #actions = [enable_version,disable_version,]

class ServersAdmin(admin.ModelAdmin):
    list_display = ["server_name","edition","service_pack","cummulative_update","tcp_port","role","Node1","Node2","is_visible"]
    #actions = [enable_server,disable_server,]
    exclude = ("is_active",)


admin.site.register(Versions,VersionsAdmin)
admin.site.register(Servers,ServersAdmin)
