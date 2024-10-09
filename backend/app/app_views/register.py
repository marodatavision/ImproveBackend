from django.shortcuts import render, redirect
from django.contrib.auth import login
from app.forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Benutzer nach der Registrierung automatisch einloggen
            return redirect('landing')  # Weiterleitung zur Startseite nach erfolgreicher Registrierung
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
