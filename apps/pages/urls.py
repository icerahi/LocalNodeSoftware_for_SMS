from django.urls import path

from apps.pages import views

urlpatterns=[
    path('',views.home,name='home'),
    path('pen/',views.pen,name='pen'),
    path('content_list/<subject>/',views.content_list,name='content_list'),
    path('content/<id>/',views.content,name='content'),
    path('notice/',views.NoticeListView.as_view(),name="notice_list"),
    path('notice/<pk>',views.NoticeDetailView.as_view(),name='notice_detail'),
    path('study/',views.study,name='study'),
    path('routine/',views.Routine.as_view(),name='routine'),
]