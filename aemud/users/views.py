from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterMembreForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterMembreForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Votre compte a bien été crée {username}')
            return redirect('index')

    else:
        form = RegisterMembreForm()

    return render(request, 'users/register_form.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
