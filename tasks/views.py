from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html',{
        "form": UserCreationForm
    })

#def signup(request):
#    return render(request, 'signup.html',{
#        "form": UserCreationForm
#    })