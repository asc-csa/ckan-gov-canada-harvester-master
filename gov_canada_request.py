# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import json
import pprint
import re
import logging
#import simplejson
import time
try:    #try to import the python 3 urllib:
    from urllib.parse import quote
    from urllib.request import urlopen, Request
except ImportError:   #revert to Python 2 libraries
    from urllib2 import urlopen, Request
    from urllib import quote

def send_request(API_KEY, CKAN_URL):
    with open('gov_canada_datasets_clean.json', 'r') as f:
        cleaned_datasets = json.load(f)

    for dataset in cleaned_datasets:
        try :
            data_string = quote(json.dumps(dataset))

            # We'll use the package_create function to create a new dataset.
            request = Request(CKAN_URL+'api/action/package_create')

            # Creating a dataset requires an authorization header.
            # Replace *** with your API key, from your user account on the CKAN site
            # that you're creating the dataset on.
            request.add_header('Authorization', API_KEY)

            # Make the HTTP request.
            response = urlopen(request, data_string)
            #response.encoding = "utf-8"
            assert response.code == 200

            # Use the json module to load CKAN's response into a dictionary.
            print(response.read)
            with open('data.txt','w') as outfile :
                json.dump(response,outfile)
            response_dict = simplejson.loads(response.read())

            print(dataset)

            if response_dict[u'success'] is False:
                logging.error('Dataset failed to upload')

            # package_create returns the created package as its result.
            created_package = response_dict[u'result']
            pprint.pprint(created_package)
        except :
            print('An error occured and this dataset will be skipped')
