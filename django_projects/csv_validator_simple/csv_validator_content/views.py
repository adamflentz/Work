# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
import validate_table, encode_dict



from wsgiref.util import FileWrapper
from forms import DocumentForm, JSONDocumentForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from goodtables import validate


import json


# Create your views here.
class HomePageView(TemplateView):
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        jsonform = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            def validate_table(request):
                if len(request.FILES) == 1:
                    jsonfile = None
                else:
                    jsonfile = request.FILES['jsonfile']
                    jsonpath = default_storage.save('tmp/jsonfile.json', ContentFile(jsonfile.read()))
                csvfile = request.FILES['docfile']
                path = default_storage.save('tmp/csvfile.csv', ContentFile(csvfile.read()))
                if jsonfile is None:
                    validator = validate(path, error_limit=1000000, row_limit=1000000)
                else:
                    validator = validate(path, error_limit=1000000, row_limit=1000000, schema=jsonpath)
                return validator
            validator_content = validate_table(request)
            print(validator_content)
            return render(request, 'home.html', {'validator_content': validator_content})
    def get(self, request):
        form = DocumentForm()  # A empty, unbound form
        jsonform = JSONDocumentForm()
        return render(request, 'home.html', {'form': form, 'jsonform': jsonform})


