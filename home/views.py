from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from lessons.forms import lessonCreationForm
from teachers.models import teacher
from teachers.forms import teacherCreationForm

@login_required(login_url='/accounts/login/')
def HomePage(request):
    context = {}
    if teacher.DoesNotExist:
        context['form'] = teacherCreationForm()
    else:
        context['form'] = lessonCreationForm()

    return render(request, "home/home_page.html", context)