from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,Group
from django.db.models import Q
from django.urls import NoReverseMatch,reverse
from server.models import Versions,Servers

# Create your models here.



class NewDatabaseManager(models.Manager):
    def requests_for_user(self,user):
        '''Return a queryset of database requests of the user'''
        return super(NewDatabaseManager,self).get_queryset().filter(Q(user_requestor_id=user.id))

class NewDatabase(models.Model):
    version = models.ForeignKey(Versions,on_delete=models.DO_NOTHING,verbose_name='Version')
    database_name = models.CharField(max_length=100,verbose_name='Database Name')
    size = models.IntegerField(verbose_name='Database Size',help_text='Keep in mind that database size must be specified in GB.')
    server_name = models.ForeignKey(Servers,on_delete=models.DO_NOTHING,verbose_name='Server Name')
    application_name = models.CharField(max_length = 100,verbose_name = "Application Name")
    team_distribution_list = models.CharField(max_length=100)
    date_requested = models.DateTimeField(editable=False,default=timezone.now)
    request_completed = models.NullBooleanField(null=True)
    log_message = models.CharField(max_length=2000,null=True)
    user_requestor = models.ForeignKey(User,related_name='new_database_user_requestor',on_delete=models.DO_NOTHING)
    is_database_created = models.NullBooleanField(null=True,verbose_name="Database Created")
    dba_approval = models.NullBooleanField(null=True,verbose_name="DBA Approval")
    manager_approval = models.NullBooleanField(null=True,verbose_name="Manager approval")
    manager_approval_id = models.ForeignKey(User,related_name='new_database_manager_approval',on_delete=models.DO_NOTHING)
    manager_approval_date = models.DateTimeField(null=True,verbose_name="Manager approval date",blank=True)
    last_email_sent = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True,blank=True)
    is_added_application_repository = models.NullBooleanField(null=True,verbose_name="Added to application repository")
    
    

    class Meta:
        verbose_name = "Database Request"
        verbose_name_plural = "Database Requests"


    objects = NewDatabaseManager()

    def get_absolute_url(self):
        return reverse('database_request_detail',args=[self.id])

    def __str__(self):
        return '{0} - {1} - {2} - {3}GB'.format(self.id,self.server_name,self.database_name,self.size)