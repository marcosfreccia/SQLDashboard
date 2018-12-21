from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test

from server.models import Servers



# Create your views here.

#Servers.objects.filter

@login_required
def servers(request):
    servers_list = Servers.objects.all()
    return render(request,'server/servers.html',{'servers_list':servers_list})