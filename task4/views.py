from django.shortcuts import render


def func_index(request):
    return render(request, 'index.html')


def func_index_1(request):
    points_list = ['Игра для взрослых', 'Игра для подростков', 'Игра для детей']
    context = {
        'points_list': points_list,
    }
    return render(request, 'index_1.html', context)


def func_index_2(request):
    return render(request, 'index_2.html')
