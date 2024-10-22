from django.shortcuts import render


def func_index(request):
    return render(request, 'index.html')


def func_index_1(request):
    return render(request, 'index_1.html')


def func_index_2(request):
    return render(request, 'index_2.html')
