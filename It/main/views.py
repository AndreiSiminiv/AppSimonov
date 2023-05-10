from django.shortcuts import render


def index (request):
    date = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj':{
            'car': "bmv",
            "age": 18,
            "hobby": "footbAL"
        }
    }
    return render(request,'main/index.html',date)

def about (request):
    return render(request,'main/about.html')