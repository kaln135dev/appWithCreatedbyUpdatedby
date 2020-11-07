from django import forms
from .models import mainModel


class mainForm(forms.ModelForm):
    class Meta:
        model = mainModel
        fields = ['main_name', 'category', 'item_one', 'item_two']
