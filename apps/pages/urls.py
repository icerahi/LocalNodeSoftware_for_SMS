from django.urls import path

from apps.pages import views

urlpatterns=[
    path('',views.home,name='home'),
    path('pen/',views.pen,name='pen'),
    path('content_list/',views.content_list,name='content_list'),
    path('content/',views.content,name='content'),
    # path('notice/',views.NoticeListView.as_view(),name="notice_list"),
    # path('notice/<pk>',views.NoticeDetailView.as_view(),name='notice_detail'),
]