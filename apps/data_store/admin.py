from django.contrib import admin

# Register your models here.
from apps.data_store.models import NodeData, Notice


@admin.register(NodeData)
class NodeDataAdmin(admin.ModelAdmin):
    list_display = ['school_name','school_id','class_name','ip_address','node_id','port','mac_address']



@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title','body',]



