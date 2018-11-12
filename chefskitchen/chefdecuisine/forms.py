from django import forms
from chefdecuisine.models import sousChef


class chefForm(forms.ModelForm):
    class Meta:
        model = sousChef
        exclude = []
        # fields = ['first_name', 'last_name']
