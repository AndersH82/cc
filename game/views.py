from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def interrogation_view(request):
    return render(request, 'interrogation.html')

def witness_suspects(request):
    return render(request, 'witness_suspects.html')