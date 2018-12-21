import django.contrib.auth.views
from django.conf.urls import url,include

import server.views

# Uncomment the next two lines to enable the admin:

urlpatterns = [
    url(r'^servers$', server.views.servers, name='servers'),
]
