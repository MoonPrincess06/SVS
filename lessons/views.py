from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from teachers.models import teacher
from .models import lesson

from .forms import lessonCreationForm

@login_required(login_url='/accounts/login/')
def lessonCreation(request):
    context = {}
    if request.method == 'POST':
        context['form'] = lessonCreationForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'Unterrichtsstunde erstellt.')
    else:
        context['form'] = lessonCreationForm()

    return render(request, "lessoncreation.html", context)

@login_required(login_url='/accounts/login/')
def lessonOverview(request):
    context = {}
    context['teachers'] = teacher.objects.all()
    context['lesson'] = lesson
    return render(request, 'lessonview.html', context)