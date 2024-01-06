from django.shortcuts import render, redirect
from random import choice


new_year_greetings = [
    "З Новим Роком! Нехай цей рік принесе вам щастя та радість!",
    "Щасливого Нового Року! Бажаємо вам яскравих святкових моментів!",
    "Новорічні вітання! Нехай вам супроводжує удача в усьому!",
    "Зичимо радості, здоров'я та успіхів у новому році!",
    "Веселих свят і щасливого Нового Року! Нехай всі ваші мрії здійсняться!",
    "Зичимо вам світлих свят та яскравих вражень у новому році!",
    "Щасливого Нового Року! Нехай кожен день буде наповнений радістю!",
    "Бажаємо вам купу радості та море веселих моментів у новому році!",
    "З новим щастям! Нехай кожен день приносить вам тільки позитивні емоції!",
    "Новорічні привітання! Нехай у вашому житті буде багато світлих подій та удачі!"
]


def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html')
    else:
        name = request.POST.get('name_inp')
        return redirect(f'/card/{name}')


def card(request, name):
    return render(request, 'main/card.html', {'message': choice(new_year_greetings), 'name': name})

