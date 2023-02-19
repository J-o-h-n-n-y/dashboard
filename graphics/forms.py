from django import forms

from .models import Budget, Direction, Region


class SearchForm(forms.ModelForm):
    direction = forms.ModelChoiceField(queryset=Direction.objects, required=False)
    region = forms.ModelChoiceField(queryset=Region.objects, required=False)
    year = forms.IntegerField(max_value=2023)

    class Meta:
        model = Budget
        fields = ["direction", "region"]

