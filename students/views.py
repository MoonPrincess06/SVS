from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from .models import student
from .forms import updateStudent, classCreationForm


@login_required(login_url='/accounts/login/')
def getStudent(request, pk):
    context={}
    context['student'] = student.objects.get(id = pk)
    context['students'] = student.objects.all().order_by('lastName')
    if request.method == 'POST':
        context['form'] = updateStudent(request.POST, request.FILES, instance=context['student'])
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'Schüler erfolgreich aktualisiert')
    else:
        context['form'] = updateStudent(instance=context['student'])
    return render(request, 'studentView.html', context)

@login_required(login_url='/accounts/login/')
def classCreation(request):
    if request.method == "POST":
        form = classCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klasse erstellt')
    else:
        form = classCreationForm()
    return render(request, 'classCreation.html', {'form':form})
