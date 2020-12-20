from os.path import basename
from urllib.parse import urlsplit
from urllib.request import urlretrieve, urlcleanup

from django.core.files import File
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from apps.data_store.models import NodeData, Notice, CourseMaterial
from apps.data_store.serializers import NodeDataSerializer, NoticeSerializer, CourseMaterialSerializer


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
#
# def download(url):
#     try:
#
#
#         return
#     finally:
#         urlcleanup()



class CourseMaterialViewSet(viewsets.ModelViewSet):
    search_fields=['content_id']
    filter_backends = [filters.SearchFilter,]
    queryset = CourseMaterial.objects.all()
    serializer_class = CourseMaterialSerializer



    def create(self, request, *args, **kwargs):
        try:
            for i in request.data:
               tempname, _ = urlretrieve(i['content'] )
               print(tempname)
               i['content']= File(open(tempname,'rb'))#it's working
               urlcleanup()

               serializer = self.get_serializer(data=request.data, many=True)
        except:
            tempname, _ = urlretrieve(request.data['content'])
            print(tempname)
            request.data['content'] = File(open(tempname, 'rb'))  # it's working
            urlcleanup()
            serializer = self.get_serializer(data=request.data)


        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)






class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data,many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



