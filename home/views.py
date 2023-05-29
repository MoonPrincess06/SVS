from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from students.forms import studentCreationForm
from students.models import student

@login_required(login_url='/accounts/login/')
def HomePage(request):

    if request.method == 'POST':
        form = studentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SCHUELER ERSTELLT WOOOOOO')
    else:
        form = studentCreationForm()

    return render(request, "home/home_page.html", {'form': form})