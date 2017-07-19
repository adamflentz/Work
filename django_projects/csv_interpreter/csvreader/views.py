# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from forms import UploadFileForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class UploadFileForm(TemplateView):
    template_name = "csvoutput.html"

    def POST(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        csvfile = request.FILES['csv_file']
        #dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        #csvfile.open()
        #reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
        #analyzer = CSVInspector()
        #analyzer.inspection(csvfile)
        hello = "howdy!"
        return render(request, "csvoutput.html", {"hello", hello})


