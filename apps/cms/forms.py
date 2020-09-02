from django import forms

from apps.problem.models import Problem
from apps.contest.models import Contest
from apps.contest.models import ContestProblem
from apps.forms import FormMixmin


class CreateProblemForm(forms.ModelForm, FormMixmin):
    test_data = forms.FileField(label=u"上传压缩包", required=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Problem
        exclude = ['in_date', 'accepted', 'submit', 'solved']


class CreateContestForm(forms.ModelForm, FormMixmin):
    password = forms.CharField(max_length=12, min_length=6, error_messages={"max_length":"密码最多不能超过12位！",
                                                                       "min_length":"密码最少不能少于6位！"})
    langmask = forms.CharField(max_length=8, min_length=1, error_messages={"max_length":"语言掩码最多不能超过8位！",
                                                                       "min_length":"语言掩码最少不能少于1位！"})

    def clean(self):
        cleaned_data = super(CreateContestForm, self).clean()

        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        time = (end_time - start_time).total_seconds()

        print('=' * 10)
        print(time)
        print('='*10)

        if time < 0:
            raise forms.ValidationError('错误：比赛结束时间早于比赛开始时间！')

    class Meta:
        model = Contest
        exclude = ['password', 'user_id']


class CreateContestProblemForm(forms.ModelForm, FormMixmin):
    class Meta:
        model = ContestProblem
        exclude = ['c_accepted', 'c_submit']

