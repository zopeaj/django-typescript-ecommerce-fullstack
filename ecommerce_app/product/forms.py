from django import forms
from product.models import ProductUploadImag


class ProductSearchForm(forms.Form):
    name = forms.TextField(widget=forms.TextInput(attrs={'type': 'text'}))
    category = forms.TextField(widget=forms.TextInput(attrs={'type': 'text'}))

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = ProductUploadImag
        fields = '__all__'

class ProductUpdateForm(forms.ModelForm):
    pass

