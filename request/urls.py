import django.contrib.auth.views
from django.contrib import admin
from django.conf.urls import url,include


import request.views
from request import views

urlpatterns = [
    # Examples:
    url(r'^admin/',admin.site.urls),
    url(r'^new_database/',request.views.new_database,name='new_database'),
    url(r'^ajax/load-servers/$', request.views.ajax_load_servers_per_version, name='ajax_load_servers_per_version'),
    url(r'^ajax/ajax_validate_database_name/$', request.views.ajax_validate_database_name, name='ajax_validate_database_name'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]