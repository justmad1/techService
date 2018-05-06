from django import forms
from django.contrib.auth.models import User

from master_office.models import Order


class FeedbackForm(forms.ModelForm):
    feedback = forms.CharField(label="Обратная связь",required=True)

    class Meta:
        model = Order
        fields = ('feedback',)

    def save(self, commit=True):
        comment = super(forms.ModelForm, self).save(commit=False)
        comment.feedback = self.cleaned_data["feedback"]
        # comment. = self.cleaned_data["first_name"]
        # user.last_name = self.cleaned_data["last_name"]
        if commit:
            comment.save()
        return comment