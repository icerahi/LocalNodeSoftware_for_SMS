from django.contrib import admin

# Register your models here.
from apps.data_store.models import NodeData, Notice, CourseMaterial


@admin.register(NodeData)
class NodeDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    pass