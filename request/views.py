import sys
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from request.models import *
from request.forms import *
from request.create_database import validate_database_name

# Create your views here.

@login_required
def new_database(request):
    if request.method == 'POST':
        try:
            newdatabaserequest = NewDatabase(user_requestor=request.user,is_database_created=0,is_email_sent=0,is_added_application_repository=0)
            form = NewDatabaseForm(data=request.POST,instance=newdatabaserequest)
            if form.is_valid():
                first_name = request.user.first_name
                last_name = request.user.last_name
                full_url = request.get_host()
                saved_model = form.save()
                request_id = {}
                request_id = saved_model.pk
                form = NewDatabaseForm()
                return render(request,'request/new_database.html',{'result': 'submitted','form':form})
        except:
            error = sys.exc_info()
    else:
        form = NewDatabaseForm()
    return render(request,'request/new_database.html',{'form':form})


def ajax_validate_database_name(request):
    database_name = request.GET.get('database_name',None)
    server_name = request.GET.get('server_name',None)
    data = validate_database_name(server_name,database_name)
    return JsonResponse(data)

def ajax_load_servers_per_version(request):
    versionid = request.GET.get('version')
    servers = Servers.objects.filter(version_id=versionid).filter(is_visible=True).order_by('server_name')
    return render(request,'request/ajax/servers_dropdown_list_options.html',{'servers':servers})