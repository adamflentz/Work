# -*- coding: utf-8 -*-

from django import forms
from validators import validate_file_extension


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
