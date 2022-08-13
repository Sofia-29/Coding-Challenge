import os
from django import forms

# Create your models here.
class DataForm(forms.Form):
    data = forms.FileField()
    targets = forms.FileField()
    model_choices = [("1", "Regression"), ("2", "Classification")]
    model_type = forms.ChoiceField(choices=model_choices)

    def file_route(self, file):
        return os.path.basename(file.name)
