from django import forms
from .models import ProductImage


# class FileFieldForm(forms.ModelForm):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta:
#         model = ProductImage
