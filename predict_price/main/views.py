from django.contrib.auth.models import User
from django.shortcuts import render

from . forms import UserForm



def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserForm()
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'main/index.html', context)

def entries_form(request):
    return render(request, 'main/entriesForm.html')