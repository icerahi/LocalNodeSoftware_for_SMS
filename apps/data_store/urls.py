from django.urls import path, include
from rest_framework import routers

from apps.data_store import views

router = routers.DefaultRouter()
router.register('node_data',views.NodeDataViewSet)
router.register('notice',views.NoticeViewSet)
router.register('course_material',views.CourseMaterialViewSet)

urlpatterns=[
    path('',include(router.urls)),
]