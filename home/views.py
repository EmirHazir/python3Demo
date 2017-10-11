from django.shortcuts import render, HttpResponse


def home_view(req):
    if req.user.is_authenticated():
        context = {
            'isim': 'Emir'
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(req, 'home.html', context)
