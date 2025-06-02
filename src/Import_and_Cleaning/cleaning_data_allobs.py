import pandas as pd

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

def dependency_ratio_old(raw_path):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    years = [str(y) for y in range(1960, 2051)]
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

    return df_long

def dependency_ratio_young(raw_path):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    years = [str(y) for y in range(1960, 2051)]
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

    return df_long

def pop_total(raw_path):
    df = pd.read_csv(raw_path, skiprows=4)

    # Normalize column names: '1960 [YR1960]' → '1960'
    df.columns = [col.split(' ')[0] if col[:4].isdigit() else col for col in df.columns]

    years = [str(y) for y in range(1960, 2051)]
    df = df[['Country Name', 'Country Code'] + years]

    df_long = df.melt(
        id_vars=['Country Name', 'Country Code'],
        var_name='Year',
        value_name='Population_Total'
    )

    df_long = df_long.rename(columns={
        'Country Name': 'Country',
        'Country Code': 'ISO3'
    })

    df_long['Country'] = df_long['Country'].replace(COUNTRY_RENAME_MAP)

    df_long['Year'] = df_long['Year'].astype(int)
    df_long = df_long.sort_values(by=['Country', 'Year']).reset_index(drop=True)

    return df_long