from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    MONTH_CHOICES = [(i, i) for i in xrange(1, 12)]
    YEAR_CHOICES = [(i, i) for i in xrange(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security Code(CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        instance.username = instance.email

        if commit:
            instance.save()
        return instance

class UserLoginForm(forms.Form):
        email = forms.EmailField()
        password = forms.CharField(widget=forms.PasswordInput)