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
    
    # Display the number of datasets
    print ('Adding new datasets to the data portal...')
    print ('Note: The existing datasets will NOT be added.')
    print ('Total number of datasets found (new & existing): ' + str(len(cleaned_datasets)) + '\n')
    nbNewDatasets = 0
    nbExistingDatasets = 0
    
    for dataset in cleaned_datasets:
        try :
            print ('Loading a dataset...')
            data_string = quote(json.dumps(dataset)).encode("utf-8")
            print ('Dataset loaded')

            # We'll use the package_create function to create a new dataset.
            request = Request(CKAN_URL+'api/action/package_create')
            print ('Dataset created')

            # Creating a dataset requires an authorization header.
            # Replace *** with your API key, from your user account on the CKAN site
            # that you're creating the dataset on.
            request.add_header('Authorization', API_KEY)
            print ('Dataset authorized')

            # Make the HTTP request.
            print ('Making the HTTP request...')
            #print (data_string)
            #print (request)
            response = urlopen(request, data_string)
            #response.encoding = "utf-8"
            print ('HTTP request... done')
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
            print ('New dataset added to the data portal')
            nbNewDatasets = nbNewDatasets + 1
            created_package = response_dict[u'result']
            pprint.pprint(created_package)
        except Exception as ex:
            errorMsg = str(ex)
            if 'CONFLICT' in errorMsg:
                nbExistingDatasets = nbExistingDatasets + 1
                print('This dataset will be skipped because it is already in the database')
            else:
                print('An error occured and this dataset will be skipped')
                print(errorMsg)
                #print(ex.message)
            print('')

    # Summary
    print('\nSUMMARY')
    print ('Number of new datasets: ' + str(nbNewDatasets))
    print ('Number of existing datasets: ' + str(nbExistingDatasets))
    print('')