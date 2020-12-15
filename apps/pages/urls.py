from django.urls import path

from apps.pages import views

urlpatterns=[
    path('',views.home,name='home'),
    path('notice/',views.NoticeListView.as_view(),name="notice_list"),
    path('notice/<pk>',views.NoticeDetailView.as_view(),name='notice_detail'),
]