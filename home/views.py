from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from students.forms import studentCreationForm
from students.models import student

@login_required(login_url='/accounts/login/')
def HomePage(request):
    context = {'students': student.objects.all().order_by('lastName')}
    if request.method == 'POST':
        context['form'] = studentCreationForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'SCHUELER ERSTELLT WOOOOOO')
    else:
        context['form'] = studentCreationForm()

    return render(request, "home/home_page.html", context)

