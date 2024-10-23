from django.shortcuts import render


def func_index(request):
    return render(request, 'index.html')


def func_index_1(request):
    point_1 = 'Игра для взрослых'
    point_2 = 'Игра для подростков'
    point_3 = 'Игра для детей'
    context = {
        'point_1': point_1,
        'point_2': point_2,
        'point_3': point_3,
    }
    return render(request, 'index_1.html', context)


def func_index_2(request):
    return render(request, 'index_2.html')
