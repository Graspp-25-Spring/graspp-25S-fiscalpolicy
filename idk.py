import requests
import pandas as pd

def download_worldbank(indicator, countries, date_start, date_end):
    url_base = 'http://api.worldbank.org/v2/'  # Base URL for the World Bank API
    country_codes = ';'.join(countries)  # Combine country codes into a string
    url = url_base + f'country/{country_codes}/indicator/{indicator}?date={date_start}:{date_end}&per_page=30000' #create the url with start and end date.
    url = url_base + f'country/{country_codes}/indicator/{indicator}?per_page=30000' # This line overrides the previous one. It will ignore start/end date.

    response = requests.get(url)  # Download data from the URL
    df = pd.read_xml(response.content)  # Convert the downloaded data to a table
    return df  # Return the table
data = download_worldbank(
    indicator = 'NY.GDP.PCAP.CD' , 
    countries = ['US', 'CA', 'MX', 'JP'],  
    date_start = '2021', 
    date_end = '2023'
)
data.head(2)
print(data)
import numpy as np
import requests
import json

def fetch_fred_data(api_key, series_id):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&file_type=json&api_key={api_key}"
    response = requests.get(url)
    dictionary = response.json()['observations']
    df = pd.DataFrame(dictionary)[['date','value']]
    df.value = df.value.replace(".", np.nan).astype(float)
    df = df.dropna()
    return df

  
# Example usage
api_key = "6290b1cc11ac06efe031863a31de166f"  # Replace with your actual API key
series_id = "GDP"  # Example series ID for US GDP
    
df = fetch_fred_data(api_key, series_id)
df.head(2)