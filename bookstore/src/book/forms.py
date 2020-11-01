from django import forms




class CreateBookForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)