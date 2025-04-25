import pandas as pd
import requests
import io

url = 'https://github.com/KMueller-Lab/Global-Macro-Database/raw/refs/heads/main/data/final/chainlinked_infl.dta'
df_macro = pd.read_stata(url)
df_macro.head(2)
url = "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB_ULC_Q,1.0/.Q.......?startPeriod=1990-Q4&format=csv"
response = requests.get(url)
data = io.StringIO(response.text)
df_oecd = pd.read_csv(data)
df_oecd.head(2)
df_macro_nz = df_macro.query("ISO3 == 'NZL'")[['ISO3', 'year', 'OECD_KEI_infl', 'BIS_infl']].dropna()
df_macro_nz.tail(2)
cols = ['REF_AREA', 'TIME_PERIOD', 'OBS_VALUE', 'MEASURE', 'UNIT_MEASURE']
df_oecd_nz = df_oecd[cols].query("REF_AREA == 'NZL' & MEASURE=='ULCE' & UNIT_MEASURE == 'PA'")
df_oecd_nz.head(2)
df_macro_nz = df_macro_nz.rename({"ISO3":'country', "year":'date'}, axis=1)
df_macro_nz.head(2)
df_oecd_nz = df_oecd_nz.rename({"REF_AREA":'country', "TIME_PERIOD":'date', 'OBS_VALUE':'ULCE'}, axis=1).drop(["MEASURE", "UNIT_MEASURE"], axis=1)
df_oecd_nz.head(2)
df_oecd_nz.date.dtype
df_oecd_nz.date = pd.PeriodIndex(df_oecd_nz.date, freq='Q').to_timestamp()
df_oecd_nz.date.dtype
df_macro_nz.date.dtype
df_macro_nz.head(2)
df_macro_nz.date = pd.to_datetime(df_macro_nz.date, format = '%Y')
df_macro_nz.date.dtype