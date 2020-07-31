import gov_canada_data_clean
import gov_canada_harvester
import gov_canada_request


API_KEY = 'acdd706b-e61d-40e5-9fe0-602a625a2496'
CKAN_URL = 'http://0.0.0.0:5000/'
org_id ='db06a8c5-1706-4f66-8b5a-25dd77a125e9'
#gov_canada_harvester.get_data()
gov_canada_data_clean.clean_data(org_id)
gov_canada_request.send_request(API_KEY, CKAN_URL)
