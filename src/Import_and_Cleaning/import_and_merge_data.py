import numpy as np
import pandas as pd

from cleaning_data import (
    clean_health_data, clean_education, dependency_ratio_data,
    dependency_ratio_old, dependency_ratio_young, GDP_percapita,
    clean_income_level, population, average_schooling,
    learning_outcome, life_expectancy, mortality, region, clean_trade_data, gov_consumption_data
)

def load_and_merge_all_data():
    df_health = clean_health_data('../data/raw/health_expenditure_raw.csv', '../data/processed/health_expenditure_clean.csv')
    df_education = clean_education('../data/raw/Education_expenditure_raw.csv', '../data/processed/Education_expenditure_clean.csv')
    df_dependency = dependency_ratio_data('../data/raw/dependency_ratio_raw.csv', '../data/processed/dependency_ratio_clean.csv')
    df_dependency_old = dependency_ratio_old('../data/raw/dependency_ratio_old_raw.csv', '../data/processed/dependency_ratio_old_clean.csv')
    df_dependency_young = dependency_ratio_young('../data/raw/dependency_ratio_young_raw.csv', '../data/processed/dependency_ratio_young_clean.csv')
    df_GDP_percapita = GDP_percapita('../data/raw/GDP_percapita.csv', '../data/processed/GDP_percapita_clean.csv')
    df_trade = clean_trade_data('../data/raw/trade_gdp.csv', '../data/processed/trade_gdp_clean.csv')
    df_gov_consumption = gov_consumption_data('../data/raw/gov_consumption_gdp.csv', '../data/processed/gov_consumption_clean.csv')
    df_population = population('../data/raw/pop_total.csv', '../data/processed/pop_total_clean.csv')
    df_income_level = clean_income_level('../data/raw/Income_level_raw.xlsx', '../data/processed/income_level_clean.csv')
    df_average_schooling = average_schooling('../data/raw/average_schooling_raw.csv', '../data/processed/average_schooling_clean.csv')
    df_learning_outcome = learning_outcome('../data/raw/learning_outcome_raw.csv', '../data/processed/learning_outcome_clean.csv')
    df_life_expectancy = life_expectancy('../data/raw/life_expectancy_raw.csv', '../data/processed/life_expectancy_clean.csv')
    df_mortality = mortality('../data/raw/mortality_raw.csv', '../data/processed/mortality_clean.csv')
    df_region = region('../data/raw/Income_level_raw.xlsx', '../data/processed/region_clean.csv')
    
    

    merged = df_health.merge(df_education, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_dependency, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_dependency_old, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_dependency_young, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_life_expectancy, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_mortality, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_average_schooling, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_learning_outcome, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_GDP_percapita, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_trade, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_gov_consumption, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_population, on=["ISO3", "Year", "Country"], how="outer")
    merged = merged.merge(df_income_level, on=["ISO3", "Country"], how="left")
    merged = merged.merge(df_region, on=["ISO3", "Country"], how="left")

    for col in [
        'Dependency_Ratio',
        'Dependency_Ratio_Old',
        'Dependency_Ratio_Young',
        'Population'
    ]:
        merged[col] = (
            merged[col]
            .astype(str)                      # ensure can run string ops
            .str.replace(',', '')             # drop thousands separators
            .str.strip()                      # drop leading/trailing spaces
            .pipe(pd.to_numeric, errors='coerce')  # convert, invalid→NaN
        )
 
    return merged
