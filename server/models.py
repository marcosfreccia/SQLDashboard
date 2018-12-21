from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

SERVER_ROLE = (('PRODUCTION','PRODUCTION'),('DEVELOPMENT','DEVELOPMENT'),('TEST','TEST'),('MANAGEMENT','MANAGEMENT'),('REPORTING','REPORTING'))

class Versions(models.Model):
    name = models.CharField(max_length=20,verbose_name="SQL Server Version")
    is_active = models.NullBooleanField(null=True,verbose_name="Active")

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"


    def get_absolute_url(self):
        return reverse('version_detail',args=[self.name])

    def __str__(self):
        return self.name

class Servers(models.Model):
    server_name = models.CharField(max_length=100,verbose_name="Server name")
    tcp_port = models.CharField(max_length=5,verbose_name="TCP Port")
    version = models.ForeignKey(Versions,null=True,on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=30,verbose_name="Server Role",choices=SERVER_ROLE)
    Node1 = models.CharField(max_length=50,null=True,verbose_name="Node 01",blank=True)
    Node2 = models.CharField(max_length=50,null=True,verbose_name="Node 02",blank=True)
    edition = models.CharField(max_length=50,blank=True,null=True,verbose_name="Edition")
    service_pack = models.CharField(max_length=5,blank=True,null=True,verbose_name="Service Pack")
    cummulative_update = models.CharField(max_length=5,blank=True,null=True,verbose_name="Cummulative Update")
    always_on_enabled = models.NullBooleanField(blank=True,null=True,verbose_name="Always ON Enabled")
    failover_clustering_enabled = models.NullBooleanField(blank=True,null=True,verbose_name="Failover Clustering Enabled")
    is_visible = models.NullBooleanField(null=True,verbose_name="Visible")
    is_active = models.NullBooleanField(null=True,verbose_name="Active",default=1)

    class Meta:
        verbose_name = "Server"
        verbose_name_plural = "Servers"


    def get_absolute_url(self):
        return reverse('server_detail',args=[self.server_name])

    def __str__(self):
        return self.server_name