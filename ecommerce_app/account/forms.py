from django import forms

class AccoutUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('user', )
