# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
class JSONDocumentForm(forms.Form):
    jsonfile = forms.FileField(
        label='Select a JSON schema file (optional)', required=False
    )
