from rest_framework import serializers

from apps.data_store.models import NodeData, Notice


class NodeDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = NodeData
        fields = ['url','node_id','ip_address','port','mac_address',
                  'school_id','school_name','class_name',]




class NoticeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notice
        fields = ['url','title','body']


