url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
key = 'CompactData/IFS/M.GB.PCPI_IX'
import requests
import pandas as pd
import json
import io
data = (requests.get(f'{url}{key}').json()
        ['CompactData']['DataSet']['Series'])
baseyr = data['@BASE_YEAR']

data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')] for obs in data['Obs']]
df = pd.DataFrame(data_list, columns=['date', 'value'])
     
df = df.set_index(pd.to_datetime(df['date']))['value'].astype('float')

df.head(2)
url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
key = 'CompactData/IFS/M..PCPI_IX.?startPeriod=2000&endPeriod=2001'

data = requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series']
#data