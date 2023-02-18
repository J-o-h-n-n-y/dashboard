from django import forms

from .models import Budget, Direction, Region


class BudgetForm(forms.ModelForm):
    direction = forms.ModelMultipleChoiceField(queryset=Direction.objects, required=False)
    region = forms.ModelMultipleChoiceField(queryset=Region.objects, required=False)

    class Meta:
        model = Budget
        fields = ["year"]
