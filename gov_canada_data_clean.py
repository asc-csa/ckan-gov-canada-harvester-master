#!/usr/bin/env python
# coding: utf-8

# ## Data Cleaning datasets from gov canada




import json
import pprint
import re
import logging

def clean_data(org_id):
    # Comments regarding this function can be found in the jupyter notebook
    with open('gov_canada_datasets_raw.json', 'r') as f:
        datasets = json.load(f)


    datasets[0][u'result']


    delete_keys = [u'creator_user_id', u'groups', u'id', u'revision_id',
                u'isopen', u'license_title', u'license_url', u'metadata_contact', u'metadata_created',
                u'metadata_modified',u'owner_org', u'num_resources', u'num_tags', u'organization']

    resource_delete_keys = [u'datastore_active', u'id', u'package_id', u'position', u'url_type']

    cleaned_datasets = []

    for dataset in datasets:
        dataset = dataset[u'result']

        for key in delete_keys:
            dataset.pop(key, None)

        for resource in dataset[u'resources']:
            for key in resource_delete_keys:
                resource.pop(key, None)

        dataset[u'owner_org'] = org_id
        dataset[u'project'] = u'unlisted'
        dataset[u'type'] = u'dataset'

        if (u'audit' in dataset[u'keywords']) or (u'evaluation' in dataset[u'keywords']) or (u"government_and_politics" in dataset[u'subject']) or  u"information_and_communication" in dataset[u"subject"]:
            dataset[u'science_admin']='False'
        else :
            dataset[u'science_admin']='True'



        #dataset[u'diids_no']=u'no'
        cleaned_datasets.append(dataset)



    with open('gov_canada_datasets_clean.json', 'w') as f:
        json.dump(cleaned_datasets, f)
