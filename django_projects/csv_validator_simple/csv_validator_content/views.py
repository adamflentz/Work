# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from wsgiref.util import FileWrapper
from forms import DocumentForm, JSONDocumentForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from goodtables import validate
import json, ast


# Create your views here.
class HomePageView(TemplateView):
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        jsonform = JSONDocumentForm(request.POST)
        if form.is_valid() and jsonform.is_valid():
            jsonfile = jsonform.cleaned_data['jsonfile']
            jsonpath = "https://raw.githubusercontent.com/" + jsonfile
            csvfile = request.FILES['docfile']
            path = default_storage.save('tmp/csvfile.csv', ContentFile(csvfile.read()))
            validator = validate(path, error_limit=1000000, row_limit=1000000, schema=jsonpath)
            return HttpResponse(json.dumps(validator))
    def get(self, request):
        form = DocumentForm()  # A empty, unbound form
        jsonform = JSONDocumentForm()
        return render(request, 'home.html', {'form': form, 'jsonform': jsonform})


