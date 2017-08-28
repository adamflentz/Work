# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
class JSONDocumentForm(forms.Form):
    jsonfile = forms.CharField(
        label='Choose a JSON file path'
    )
