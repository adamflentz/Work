# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from forms import DocumentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from goodtables import validate
import csv, codecs

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
        validator = validate(csvfile)
        content = csv.DictReader(csvfile)
        reader = csv.reader(csvfile)
        csvcontent = list(reader)

        return render(request, 'csvoutput.html', {'csv': csvfile, 'csvcontent': csvcontent, 'validator': validator})


