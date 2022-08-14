import os
from django import forms

# Create your models here.
class DataForm(forms.Form):
    data = forms.FileField(widget=forms.FileInput(attrs={'class': 'custom-file-input', 'label':'Select file'}))
    targets = forms.FileField(widget=forms.FileInput(attrs={'class': 'custom-file-input', 'label':'Select file'}))
    model_choices = [("1", "Regression"), ("2", "Classification")]
    model_type = forms.ChoiceField(choices=model_choices, widget=forms.Select(attrs={'class': 'custom-select', 'label':'Choose'}))

    def file_route(self, file):
        return os.path.basename(file.name)
