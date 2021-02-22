from urllib.request import urlretrieve

from ckeditor.fields import RichTextField
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
    body = RichTextField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


def content_file_name(instance,filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.pk}.mp4'
    return filename

class CourseMaterial(models.Model):
   # content_id = models.IntegerField(unique=True,null=True,blank=True)
    class_name = models.CharField(max_length=20)
    subject    = models.CharField(max_length=50)
    unit       = models.CharField(max_length=200)
    unit_name  = models.TextField()
    content    = models.FileField(upload_to=content_file_name)

    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.subject}-{self.unit}'

    class Meta:
            ordering = ['created']
            # constraints=[
            #     models.UniqueConstraint(
            #         fields=['subject','unit','unit_name'],
            #         name= "content can't be same"
            #     )
            # ]



class Routine(models.Model):
    subject = models.CharField(max_length=200)
    day     = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject}/{self.day}/{self.start_time}-{self.end_time}'

    class Meta:
        ordering = ['start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['subject', 'day', 'start_time','end_time'],
                name='unique data with  subject and day,start_time,end_Time'
            ),
            ]
