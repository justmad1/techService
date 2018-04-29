from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from master_office.models import OrderLine, Order, Service
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Имя', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    error_css_class = 'error'
    required_css_class = 'required'


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        group = Group.objects.get(name='ServiceClient')
        user.groups.add(group)

        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user




class OrderLineForm(forms.ModelForm):
    # service = forms.ModelChoiceField(queryset = Service.objects.all())

    class Meta:
        model = OrderLine
        fields = ['service', 'brand_name', 'device_name', 'serial_id', 'trouble_description']

    def save(self, commit=True):
        line = super(forms.ModelForm, self).save(commit=False)
        # line.service = self.cleaned_data["service"]
        if commit:
            line.save()
        return line

