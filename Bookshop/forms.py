from django.forms import ModelForm
from .models import Account
from django.contrib.auth.hashers import make_password

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'address']
