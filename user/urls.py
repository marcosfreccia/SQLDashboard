import django.contrib.auth.views
from django.contrib import admin
from django.conf.urls import url,include


import user.views

urlpatterns = [
    # Examples:
    url(r'^admin/',admin.site.urls),
    url(r'^home$', user.views.home, name='user_home'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]