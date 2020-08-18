import gov_canada_data_clean
import gov_canada_harvester
import gov_canada_request


API_KEY = '52638bb3-cf19-4372-a64d-211e79e71484'
CKAN_URL = 'http://0.0.0.0:5000/'
org_id ='95F65CF9-ED6A-4630-9C1A-8339FDB15CF0'
#gov_canada_harvester.get_data()
gov_canada_data_clean.clean_data(org_id)
gov_canada_request.send_request(API_KEY, CKAN_URL)
