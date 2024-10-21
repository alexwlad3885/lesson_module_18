from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def func_perf(request):
    return render(request, 'func_template.html')


class ClassPerf(TemplateView):
    template_name = 'class_template.html'
