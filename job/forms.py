from django import forms

from .models import Apllyjob

class Applyform(forms.ModelForm):
    class Meta:
        model = Apllyjob
        fields = ['name','email','website','cv','cover_letter']