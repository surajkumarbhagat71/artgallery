from django import forms
from .models import *

class OnerForm(forms.ModelForm):
    class Meta:
        model = Oner
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

