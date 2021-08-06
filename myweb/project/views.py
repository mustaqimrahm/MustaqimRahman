from django.shortcuts import render
from django.http import HttpResponse #Mus

from .forms import NameForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

#Mus
def index(request):
    form = NameForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(name)
            print(email)
            print(message)

    return render(request, 'first_web/index.html', {'form':form})

def heart_disease(request):
    return render(request, 'first_web/heart_disease.html')

#Mus
#def help(request):
#    help_dict = {'help_insert':'This is a HELP page'}
#    return render(request, 'first_web/help.html', context = help_dict)
