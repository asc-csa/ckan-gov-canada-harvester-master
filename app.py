import gov_canada_data_clean
import gov_canada_harvester
import gov_canada_request


API_KEY = '7b6d0045-0d10-4667-ab59-53cb84c6eda6'
CKAN_URL = 'http://127.0.0.1:5000/' 

gov_canada_harvester.get_data()
gov_canada_data_clean.clean_data()
gov_canada_request.send_request(API_KEY, CKAN_URL)
