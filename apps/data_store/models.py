from django.db import models

# Create your models here.

class NodeData(models.Model):
    node_id = models.IntegerField(unique=True)
    ip_address = models.GenericIPAddressField(unique=True)
    port    = models.IntegerField(null=True,blank=True)
    mac_address = models.CharField(max_length=50,null=True,blank=True)

    school_id = models.IntegerField(null=True,blank=True)
    school_name = models.CharField(max_length=100)
    class_name  = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if NodeData.objects.count() > 0:
            return False  # or you can raise validation error
        else:
            super(NodeData, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

class Notice(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


