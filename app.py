import gov_canada_data_clean
import gov_canada_harvester
import gov_canada_request

# Enter your API_KEY here
API_KEY = ''
CKAN_URL = 'http://0.0.0.0:5000/'
org_id ='csa-asc'
gov_canada_harvester.get_data()
gov_canada_data_clean.clean_data(org_id)
#gov_canada_request.send_request(API_KEY, CKAN_URL)
