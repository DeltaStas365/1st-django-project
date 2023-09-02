from django.http import HttpResponse
from django.shortcuts import render

def ex_ussr(request):
    country = ['Russia', 'Ukraine', 'Belarus', 'Kazakhstan', 'Lithuania', 'Latvia', 'Estonia',
        'Moldova', 'Armenia', 'Azerbaycan', 'Georgia', 'Tajikistan && other stan countries except Afg and Paki stans']


    return render(request, 'games/index.html', {'ex_ussr_countries': country, })
