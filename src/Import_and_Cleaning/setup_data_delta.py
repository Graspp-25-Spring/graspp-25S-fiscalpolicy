
import pandas as pd
import numpy as np
from cleaning_data_allobs import dependency_ratio_old, dependency_ratio_young, pop_total

#Data for bubble visaul
def prepare_change_df():
    # Load and merge
    df_old = dependency_ratio_old("../data/raw/secondary/age_dependency_old_raw.csv")
    df_young = dependency_ratio_young("../data/raw/secondary/age_dependency_young_raw.csv")
    df_pop = pop_total("../data/raw/secondary/pop_tot_raw.csv")

    merged = pd.merge(df_old, df_young, on=["ISO3", "Year", "Country"], how="outer")
    merged = pd.merge(merged, df_pop, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged[merged['ISO3'].notna()]

    # Keep 1960 and 2050 only
    df_delta = merged[merged['Year'].isin([1960, 2050])].copy()
    for col in ['Dependency_Ratio_Old', 'Dependency_Ratio_Young']:
        df_delta[col] = pd.to_numeric(df_delta[col], errors='coerce')

    # Pivot and compute delta
    pivoted = df_delta.pivot(index='Country', columns='Year', values=['Dependency_Ratio_Old', 'Dependency_Ratio_Young'])
    pivoted.columns = [f"{var}_{year}" for var, year in pivoted.columns]
    pivoted['Delta_Old'] = pivoted['Dependency_Ratio_Old_2050'] - pivoted['Dependency_Ratio_Old_1960']
    pivoted['Delta_Young'] = pivoted['Dependency_Ratio_Young_2050'] - pivoted['Dependency_Ratio_Young_1960']
    change_df = pivoted[['Delta_Old', 'Delta_Young']].dropna().reset_index()

    # Add log population 2050
    pop_2050 = merged[merged['Year'] == 2050][['Country', 'Population_Total']].copy()
    pop_2050['Population_Total'] = pd.to_numeric(pop_2050['Population_Total'], errors='coerce')
    pop_2050['Log_Population'] = np.log(pop_2050['Population_Total'])
    change_df = pd.merge(change_df, pop_2050[['Country', 'Log_Population']], on='Country', how='left')

    return change_df

#Data for timeline selected countries
def prepare_data_dependency():
    # Load and merge
    df_old = dependency_ratio_old("../data/raw/secondary/age_dependency_old_raw.csv")
    df_young = dependency_ratio_young("../data/raw/secondary/age_dependency_young_raw.csv")
    df_pop = pop_total("../data/raw/secondary/pop_tot_raw.csv")

    merged = pd.merge(df_old, df_young, on=["ISO3", "Year", "Country"], how="outer")
    merged = pd.merge(merged, df_pop, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged[merged['ISO3'].notna()]

    data_dependency = merged

    return data_dependency

def get_selected_dependency_data(selected_codes=None):
    if selected_codes is None:
        selected_codes = ['CHN', 'IDN', 'JPN', 'EUU', 'USA', 'THA', 'VNM']

    df = prepare_data_dependency()
    df = df[df['ISO3'].isin(selected_codes)].copy()
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Dependency_Ratio_Old'] = pd.to_numeric(df['Dependency_Ratio_Old'], errors='coerce')
    df = df.dropna(subset=['Year', 'Dependency_Ratio_Old'])

    iso3_to_country = {
        'CHN': 'China',
        'IDN': 'Indonesia',
        'JPN': 'Japan',
        'EUU': 'Europe',
        'USA': 'US',
        'THA': 'Thailand',
        'VNM': 'Vietnam'
    }
    df['Country_Name'] = df['ISO3'].map(iso3_to_country)

    return df
