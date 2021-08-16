import json
from c_bls_data_api import c_bls_data_api

# Call c_bls_data_api.py with a request for CPI data from 2002 through 2021
# and the name of the file to store the returned JSON data structure in.

print("Program started.")

# Set the register, series ID for CPI, start year, end year, and calculations. Note that setting calculations to true
# returns CPI percentages as well as the raw CPI.

parameters = json.dumps({"registrationkey":"0cc525c07f824fb2946765a8e18a18a7", "seriesid":['CUUR0000SA0'], "startyear":"2002", "endyear":"2021", "calculations":"true"})

# Call the bls data api class with the parameters and the name of the data output file.
c_bls_data_api(parameters, 'D:/project_data/cpi/cpi_data_report.json')

print("Program completed")