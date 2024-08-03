from django.forms import ModelForm
from .models import Movieinfo
class Movieform(ModelForm):
    class Meta:
        model=Movieinfo
        fields='__all__'