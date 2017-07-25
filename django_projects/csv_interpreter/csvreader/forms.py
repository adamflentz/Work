# -*- coding: utf-8 -*-

from django import forms
from validators import validate_file_extension


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
class JSONDocumentForm(forms.Form):
    jsonfile = forms.FileField(
        label='Select a JSON schema file (optional)', required=False
    )
