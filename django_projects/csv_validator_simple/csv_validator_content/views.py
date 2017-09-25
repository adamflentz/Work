# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseBadRequest
from goodtables import validate
import json, sys, os

# Create your views here.
class ParseContentView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    allowed_requests = ['jsonfile', 'docfile', 'error_limit', 'order_fields']

    def get(self, request):
        return HttpResponseBadRequest("400 Error: Must use POST to validate file\n", status=400)
    def post(self, request):
        # if data or json file aren't given, throw 400 error
        # if key not used in parsing file, throw 400 error
        error_limit_form = sys.maxint
        order_fields_form = True
        for key in request.data:
            if key not in self.allowed_requests:
                return HttpResponseBadRequest("400 Error: {key_name} not allowed as parameter.\n".format(key_name=key), status=400)
        if 'jsonfile' not in request.data:
            return HttpResponseBadRequest("400 Error: Payload Incorrect\n", status=400)
        elif 'docfile' not in request.data:
            return HttpResponseBadRequest("400 Error: Payload Incorrect\n", status=400)
        elif request.data['docfile'].name.endswith('.csv') == False:
            return HttpResponseBadRequest("400 Error: Data was not of CSV type\n", status=400)
        elif request.data['jsonfile'].name.endswith('.json') == False:
            return HttpResponseBadRequest("400 Error: Schema was not of JSON type\n", status=400)
        jsonfile = request.data['jsonfile']
        csvfile = request.data['docfile']
        if 'error_limit' in request.data:
            if request.data['error_limit'] == 'True':
                error_limit_form = 1
            elif request.data['error_limit'] == 'False':
                error_limit_form = sys.maxint
        if 'order_fields' in request.data:
            if request.data['order_fields'] == 'True':
                order_fields_form = True
            elif request.data['order_fields'] == 'False':
                order_fields_form = False

        #validate file if no errors have been given
        path = default_storage.save('tmp/csvfile.csv', ContentFile(csvfile.read()))
        jsonpath = default_storage.save('tmp/jsonfile.json', ContentFile(jsonfile.read()))
        jsonreader = open(jsonpath, 'r')
        jsonstring = jsonreader.read()
        try:
            json_object = json.loads(jsonstring)
            print(json_object)
        except:
            return HttpResponseBadRequest("400 Error: JSON File was not valid\n", status=400)

        jsonreader.close()
        print(jsonreader)
        validator = validate(path, error_limit=error_limit_form, row_limit=sys.maxint, schema=jsonpath, order_fields=True)
        os.remove(jsonpath)
        os.remove(path)
        return Response(json.dumps(validator))