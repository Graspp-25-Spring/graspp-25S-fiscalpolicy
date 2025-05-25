import pandas as pd

SELECTED_COUNTRIES = [
    'ARG', 'AUS', 'ARM', 'BGD', 'BRA', 'CAN', 'CHL', 'CHN', 'CYP', 'CZE', 'ECU', 'EGY', 'ETH',
    'DEU', 'GRC', 'GBR', 'GTM', 'IRL', 'IDN', 'IND', 'IRN', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'LBN',
    'MEX', 'MYS', 'MNG', 'MAR', 'MMR', 'NLD', 'NZL', 'NIC', 'NGA', 'PAK', 'PER', 'PHL', 'ROU',
    'RUS', 'SGP', 'SRB', 'SVK', 'KOR', 'TJK', 'THA', 'TUR', 'TUN', 'UKR', 'USA', 'URY', 'UZB', 'VNM'
]

COUNTRY_RENAME_MAP = {
    'Egypt, Arab Rep.': 'Egypt',
    'Iran, Islamic Rep.': 'Iran',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Korea, Rep.': 'South Korea',
    'Russian Federation': 'Russia',
    'Slovak Republic': 'Slovakia',
    'Turkiye': 'Turkey',
    'Viet Nam': 'Vietnam'
}

def dependency_ratio_data(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Dependency_Ratio'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def dependency_ratio_old(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Dependency_Ratio_Old'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def dependency_ratio_young(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Dependency_Ratio_Young'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def clean_health_data(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Health_Expenditure'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def clean_education(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Education_Expenditure'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long


def GDP_percapita(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='GDP_percapita'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def clean_income_level(raw_path, output_path, countries=SELECTED_COUNTRIES):
    # Load the Excel file
    df = pd.read_excel(raw_path)

    # Select and rename relevant columns
    df_clean = df[['Economy', 'Code', 'Income group']].rename(columns={
        'Economy': 'Country',
        'Code': 'ISO3',
        'Income group': 'income_level'
    })

    # Filter only selected countries
    df_filtered = df_clean[df_clean['ISO3'].isin(countries)]

    # Rename country names using the defined mapping
    df_filtered['Country'] = df_filtered['Country'].replace(COUNTRY_RENAME_MAP)

    # Save cleaned file
    df_filtered.to_csv(output_path, index=False)

    return df_filtered


def population(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Population'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def population_projection_full(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(1960, 2051)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Population'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def average_schooling(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path)

    # Filter to selected countries
    df = df[df['Code'].isin(countries)]

    # Filter to years between 2000 and 2023
    df = df[(df['Year'] >= 2000) & (df['Year'] <= 2022)]

    # Rename columns for clarity
    df = df.rename(columns={
        'Entity': 'Country',
        'Code': 'ISO3',
        'Average years of schooling': 'average_schooling'
    })

    # Ensure Year is integer
    df['Year'] = df['Year'].astype(int)

    # Sort for consistency
    df = df.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    # Save cleaned version
    df.to_csv(output_path, index=False)

    return df

def learning_outcome(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path)

    # Filter to selected countries
    df = df[df['Code'].isin(countries)]

    # Filter to years between 2000 and 2023
    df = df[(df['Year'] >= 2000) & (df['Year'] <= 2022)]

    # Rename columns for clarity
    df = df.rename(columns={
        'Entity': 'Country',
        'Code': 'ISO3',
        'Harmonized test scores': 'test_scores'
    })

    # Ensure Year is integer
    df['Year'] = df['Year'].astype(int)

    # Sort for consistency
    df = df.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    # Save cleaned version
    df.to_csv(output_path, index=False)

    return df

def life_expectancy(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Life_Expectancy'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long

def mortality(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2023)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Mortality_Rate'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    df_long.to_csv(output_path, index=False)
    return df_long