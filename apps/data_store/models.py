from urllib.request import urlretrieve

from django.core.files import File
from django.db import models

# Create your models here.
from rest_framework.exceptions import ValidationError


class NodeData(models.Model):
    node_id = models.IntegerField(unique=True)
    ip_address = models.GenericIPAddressField(unique=True)
    port    = models.IntegerField(null=True,blank=True)
    mac_address = models.CharField(max_length=50,null=True,blank=True)

    school_id = models.IntegerField(null=True,blank=True)
    school_name = models.CharField(max_length=100)
    class_name  = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

#store only one object in model
    def save(self, *args, **kwargs):
        if not self.pk and NodeData.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one NodeData instance')
        return super(NodeData, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']

class Notice(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.pk}.mp4'
    return filename

class CourseMaterial(models.Model):
    class_name = models.CharField(max_length=30)
    subject    = models.CharField(max_length=50)
    unit       = models.CharField(max_length=200)
    unit_name  = models.TextField()
    content    = models.FileField(upload_to=content_file_name)

    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=['class_name','subject','unit'],
                name= "content can't be same"
            )
        ]

