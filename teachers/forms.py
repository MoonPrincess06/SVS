from django.forms import ModelForm
from .models import teacher


class teacherCreationForm(ModelForm):
    class Meta:
        model = teacher
        fields = "__all__"