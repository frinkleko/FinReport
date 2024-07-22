import requests
import json

# iFinD API URL
url = "https://quantapi.51ifind.com/api/v1/basic_data_service"

# Headers including the access token
headers = {
    "Content-Type": "application/json",
    "access_token": "your_access_token_here"
}

# Form data with the stock codes and indicators
form_data = {
    "codes":
    "your_stock_codes_here",  # e.g., "600028.SH,600030.SH,600031.SH"
    "indipara": [
        {
            "indicator": "your_indicator_here",
            "indiparams": ["your_parameters_here"]
        },  # e.g.{"indicator": "ths_dividend_benchmark_shares_stock", "indiparams": ["104"]},
        {
            "indicator":
            "your_indicator_here",
            "indiparams": [
                "your_date_1_here", "your_date_2_here",
                "your_additional_parameter_here"
            ]
        },  #  {"indicator": "ths_unit_total_cash_dividend_stock", "indiparams": ["20240722", "20240722", "OC"]}
    ]
}

# Sending POST request to the API
response = requests.post(url, headers=headers, data=json.dumps(form_data))

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    data = response.json()
    # Saving the response data to a file
    with open('dividend_data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Data fetched and saved to dividend_data.json")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response: {response.text}")
