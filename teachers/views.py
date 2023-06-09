from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import teacherCreationForm
from .models import teacher

@login_required(login_url='/accounts/login/')
def TeachersPage(request):
    context = {'teachers': teacher.objects.all(), 'pk': teacher.id}
    if request.method == 'POST':
        context['form'] = teacherCreationForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'Lehrer wurde erstellt')
    else:
        context['form'] = teacherCreationForm()

    return render(request, "teachercreation.html", context)

def getTeacher(request, pk):
    context={}
    context['teacher'] = teacher.objects.get(id = pk)
    context['teachers'] = teacher.objects.all().order_by('lastName')
    return render(request, 'teacherview.html', context)