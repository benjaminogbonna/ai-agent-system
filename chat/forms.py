from django import forms
from .models import UploadedDocument

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['file']
