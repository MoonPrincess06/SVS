from django.shortcuts import render
from django.contrib import messages

from .models import student
from .forms import updateStudent


def getStudent(request, pk):
    context={}
    context['student'] = student.objects.get(id = pk)
    context['students'] = student.objects.all()
    if request.method == 'POST':
        context['form'] = updateStudent(request.POST, request.FILES, instance=context['student'])
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'Schüler erfolgreich aktualisiert')
    else:
        context['form'] = updateStudent(instance=context['student'])
    return render(request, 'studentView.html', context)
# Create your views here.
