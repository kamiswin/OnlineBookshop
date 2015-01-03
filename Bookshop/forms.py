from django.forms import ModelForm
from .models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'address']
