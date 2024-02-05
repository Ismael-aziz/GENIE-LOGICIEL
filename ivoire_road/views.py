from django.shortcuts import render

def home(request):
    return render(request, 'ivoire_road/index.html')

def chargement(request):
    return render(request, 'ivoire_road/chargement.html')
