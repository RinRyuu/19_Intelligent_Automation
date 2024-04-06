from django.shortcuts import render


# Create your views here.


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'sign_up.html')

def profile(request):
    return render(request, 'profile.html')

   
def chatbot(request):
    return render(request, 'index.html')