from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.data_store.models import NodeData, Notice
from apps.data_store.serializers import NodeDataSerializer, NoticeSerializer


class NodeDataViewSet(viewsets.ModelViewSet):
    queryset = NodeData.objects.all()
    serializer_class = NodeDataSerializer

    def create(self, request, *args, **kwargs):
       # request.data['school_name']="Bangladesh" #it's working
       # print(request.data)
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer



