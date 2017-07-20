# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from forms import DocumentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from goodtables import validate
import csv, codecs, os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

# Create your views here.
class HomePageView(TemplateView):
    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse('output'))
    def get(self, request):
        form = DocumentForm()  # A empty, unbound form
        return render(request, 'index.html', {'form': form})

class AboutPageView(TemplateView):
    template_name = "about.html"

class UploadFileForm(TemplateView):
    template_name = "csvoutput.html"

    def post(self, request):
        csvfile = request.FILES['docfile']
        path = default_storage.save('tmp/csvfile.csv', ContentFile(csvfile.read()))
        reader = csv.reader(csvfile)
        csvcontent = list(reader)
        validator = validate(path, error_limit=1000000, row_limit=1000000)

        return render(request, 'csvoutput.html', {'csv': csvfile, 'csvcontent': csvcontent, 'validator': validator})


