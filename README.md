## Government of Canada Open Data Portal Harvester

This repository harvests CSA metadata for datasets from [Government of Canada Open Data Portal](https://open.canada.ca/en/open-data)

Running this script requires that you have extended the scheming of CKAN with the custom scheming implemented in [ckanext-csa](https://gccode.ssc-spc.gc.ca/csa-data-centre-of-expertise/ckanext-csa).

Harvesting in this case means that it takes the data from the GC website and exports that locally where the script is run from, then pushes those datasets to the CKAN instance.

Once harvested it cleans the data to match CSA metadata schema, and then through CKAN's API imports those datasets into CSA CKAN.

Written in Python 2 because Python 3 was not available on the development machine I was using. CKAN is also still using Python 2.

For a closer look on the cleaning process you can download jupyter notebook and open gov_canada_data_clean.ipynb

The more updated and correct code will be in the .py file instead of the .ipynb file. If you are not familiar with jupyter notebooks, you need to install jupyter, navigate to the directory, and then launch jupyter notebook by the command `jupyter notebook`

### Quick Start

#### 1. Install the requirements with pip
Install the requirements from the requirements.txt file
```
pip install -r requirements.txt
```

#### 2. Set the configuration
In app.py replace {your_api_key} with your API key found on your CKAN user profile and replace {ckan_url} with the url of your ckan instance. The current url/IP in the file should work with the default install.

#### 3. Execute the script
Run the script with the command below. Make sure the CKAN server is running when you run this script. The script will take some time to execute all the API requests.
```
python app.py
```

#### 4. Expected Behavior and Common Mistakes
##### Common Mistakes
- The server is not running at the same time as the script
- There could also be datasets already in CKAN that share the name
- Validator errors which should show up the CKAN server console
- If the script fails to pull from the Gov Canada website it could be that their API/URL changed or that their service is down

##### Expected Behavior
If everything was imported correctly into CKAN there should be no errors when looking at the logging/alerts that are printed from the terminal which CKAN was started in.