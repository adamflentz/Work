# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv, codecs

from django.shortcuts import render
from django.views.generic import TemplateView
from forms import UploadFileForm
from inspector import CSVInspector

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class UploadFileForm(TemplateView):
    template_name = "csvoutput.html"

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        csvfile = request.FILES['csv_file']
        #dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        #csvfile.open()
        #reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        analyzer = CSVInspector()
        analyzeroutput = analyzer.inspection(csvfile)
        return render(request, "csvoutput.html", {"inspector": analyzeroutput})


