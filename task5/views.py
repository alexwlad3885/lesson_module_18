from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse


def sign_up_by_django(request):
    users = ['Anton', 'Kolya', 'Dima']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        if username in users:
            info['Error'] = 'Пользователь уже существует'
            return HttpResponse("Пользователь уже существует")
        elif password != repeat_password:
            info['Error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['Error'] = 'Вы должны быть старше 18 лет'
            return HttpResponse('Вы должны быть старше 18')
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')

    else:
        form = UserRegister()

    context = {'info': info, 'form': form}
    return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    users = ['Anton', 'Kolya', 'Dima']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['Error'] = 'Пользователь уже существует'
            return HttpResponse("Пользователь уже существует")
        elif password != repeat_password:
            info['Error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['Error'] = 'Вы должны быть старше 18 лет'
            return HttpResponse('Вы должны быть старше 18')
        else:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')

    context = {'info': info}
    return render(request, 'registration_page.html', context)