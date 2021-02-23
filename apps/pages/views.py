from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.data_store.models import Notice, CourseMaterial, Routine


def home(request):
    subjects = set(CourseMaterial.objects.values_list('subject',flat=True))
    context = {'subjects':subjects}
    return render(request,'home.html',context)

def pen(request):
    return render(request,'pen.html')

def content_list(request,subject):
    content_list = CourseMaterial.objects.filter(subject=subject)
    context = {
        'object_list':content_list,
        'subject':subject,

    }
    return render(request,'content_list.html',context)

def content(request,id):
    content = get_object_or_404(CourseMaterial,id=id)
    context={
        'object':content,
    }
    return render(request,'content.html',context)

class NoticeListView(ListView):
    template_name = 'notice_list.html'
    model = Notice

class NoticeDetailView(DetailView):
    template_name = "notice_detail.html"
    model = Notice

def study(request):
    subjects = set(CourseMaterial.objects.values_list('subject',flat=True))
    context = {'subjects': subjects}
    return render(request,'study.html',context)

class RoutineView(ListView):
    model = Routine
    template_name = 'routine.html'

    def get_context_data(self,**kwarg):
        context=super(RoutineView, self).get_context_data(**kwarg)

        context['days']=set(Routine.objects.values_list('day',flat=True))
        return context

