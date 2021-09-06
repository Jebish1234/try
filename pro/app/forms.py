
from django.forms.forms import Form 
from django.forms import ModelForm
from .models import Jobs

class Create(ModelForm):
    class Meta:
        model = Jobs
        fields = ('name',"title")