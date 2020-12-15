from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.data_store.models import Notice, CourseMaterial


def home(request):
    context={"content":CourseMaterial.objects.first()}
    return render(request,'home.html',context=context)


class NoticeListView(ListView):
    template_name = 'notice_list.html'
    model = Notice

class NoticeDetailView(DetailView):
    template_name = "notice_detail.html"
    model = Notice