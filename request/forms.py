import datetime

from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from server.models import Versions,Servers
from request.models import NewDatabase
from crispy_forms.helper import FormHelper
from bootstrap_datepicker_plus import DatePickerInput,TimePickerInput




class NewDatabaseForm(ModelForm):
    version = forms.ModelChoiceField(queryset=Versions.objects.filter(is_active=True).order_by('name'),label="")
    database_name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    application_name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number','min':0,'max':50}))
    server_name = forms.CharField(widget=forms.Select(),label="")
    team_distribution_list = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    class Meta:
        model = NewDatabase
        exclude = ['user_requestor','request_completed','log_message','is_database_created','dba_approval','is_email_sent','manager_approval','last_email_sent','date_processed','manager_email_approval','is_added_application_repository','manager_approval_date']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['server_name'].queryset = Servers.objects.none()

        if 'version' in self.data:
            try:
                version = int(self.data.get('version'))
                self.fields['server_name'].queryset = Servers.objects.filter(version_id=version).order_by('server_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty permission queryset
        elif self.instance.pk:
            self.fields['server_name'].queryset = self.instance.versions.servers_set.order_by('server_name')
