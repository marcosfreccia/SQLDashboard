from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView

from datetime import datetime

import server
import request
import user


from request import urls
from request import views

from user import urls
from user import views

from server import urls




# Uncomment the next lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^admin/',admin.site.urls),
    url(r'^$',user.views.home,name='home'),
    url(r'^request/', include(request.urls)),
    url(r'^user/', include(user.urls)),
    url(r'^server/', include(server.urls)),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$',LogoutView.as_view(),{'next_page':'home'}, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
