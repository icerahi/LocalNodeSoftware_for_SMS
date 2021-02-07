from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.data_store.models import Notice, CourseMaterial


def home(request):
    return render(request,'home.html')

def pen(request):
    return render(request,'pen.html')

def content_list(request):
    return render(request,'content_list.html')

def content(request):
    return render(request,'content.html')

class NoticeListView(ListView):
    template_name = 'notice_list.html'
    model = Notice

class NoticeDetailView(DetailView):
    template_name = "notice_detail.html"
    model = Notice


