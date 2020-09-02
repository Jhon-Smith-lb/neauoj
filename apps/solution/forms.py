from django import forms

from .models import Solution
from apps.forms import FormMixmin


class CreateSolutionForm(forms.ModelForm, FormMixmin):
    code = forms.CharField()

    class Meta:
        model = Solution
        fields = ['user_id', 'problem_id', 'nick', 'language', 'contest_id', 'num']
