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

def dependency_ratio_data_future(raw_path, output_path, countries=SELECTED_COUNTRIES):
    df = pd.read_csv(raw_path, skiprows=4)

    df = df[df['Country Code'].isin(countries)]

    years = [str(y) for y in range(2000, 2051)]
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