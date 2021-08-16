import requests
import json

class c_bls_data_api:
    
    """
        File name:      c_bls_data_api.py
        Class name:     c_bls_data_api
        Author:         Randy Runtsch
        Date:           August 12, 2021
        Description:    Call BLS Data API with a query and handle the results.
        Reference:      https://www.bls.gov/developers/api_python.htm
    """

    def __init__(self, parameters, json_file_nm):

        # Open the output JSON file, get the report from api.bls.gov, and close the output file.

        json_file = open(json_file_nm, 'w', encoding='utf-8')
        self.get_report(parameters, json_file)
        json_file.close()

    def get_report(self, parameters, json_file):

        # Call the API to get the report. Write it to a JSON file.

        headers = {'Content-type': 'application/json'}
 
        response = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data = parameters, headers = headers)

        if response.status_code != 200:
            # Something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
       
        json.dump(response.json(), json_file, indent = 6)


