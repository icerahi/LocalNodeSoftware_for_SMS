from urllib.request import urlretrieve

from django.core.files import File
from rest_framework import serializers

from apps.data_store.models import NodeData, Notice, CourseMaterial


class NodeDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NodeData
        fields = ['url','node_id','ip_address','port','mac_address',
                  'school_id','school_name','class_name',]




class NoticeSerializer(serializers.HyperlinkedModelSerializer):

    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(NoticeSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Notice
        fields = ['url','title','body']


class CourseMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseMaterial
        fields =['url','subject','unit','unit_name','content']



