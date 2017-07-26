# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from forms import DocumentForm, JSONDocumentForm
from goodtables import validate

# Create your views here.
class HomePageView(TemplateView):
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        jsonform = DocumentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            self.validate(request)
            return HttpResponseRedirect(reverse('home'))
    def get(self, request):
        form = DocumentForm()  # A empty, unbound form
        jsonform = JSONDocumentForm()
        return render(request, 'home.html', {'form': form, 'jsonform': jsonform})

    def validate(self, request):
        print("hello ")
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

        print(validator)
        return