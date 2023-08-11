from django import forms
from .models import LotteryEntry
from django import forms
class LotteryEntryForm(forms.ModelForm):
    class Meta:
        model = LotteryEntry
        fields = '__all__'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField()
