from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ["username", "last_name", "email", "password1", "password2"]

    def save(self, commit = True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    def clean_email(self):
        if User.objects.filter(email = self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

class LogInForm(AuthenticationForm):


    class Meta:
        model = User
        fields = ["username", "password"]