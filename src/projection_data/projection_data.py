import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def project_gdp_and_trade(input_path="../data/interim/merged_data.csv"):
    # Load data
    df = pd.read_csv(input_path)

    # Create log of GDP per capita
    df["log_GDP_percapita"] = np.log(df["GDP_percapita"])

    results = []

    # Loop by country
    for country, group in df.groupby("Country"):
        group = group.sort_values("Year").copy()

        # Historical sample up to 2022
        train = group[(group["Year"] < 2023) & 
                      group["log_GDP_percapita"].notna() &
                      group["trade_gdp"].notna()]

        if len(train) >= 5:
            # 1) Fit log-GDP trend
            X_train = train[["Year"]]
            y_gdp   = train["log_GDP_percapita"]
            gdp_model = LinearRegression().fit(X_train, y_gdp)

            # 2) Fit trade_gdp trend
            y_trade = train["trade_gdp"]
            trade_model = LinearRegression().fit(X_train, y_trade)

            # Prepare the "future" slice
            future = group[group["Year"] >= 2023].copy()
            X_future = future[["Year"]]

            # Predict and fill
            future["log_GDP_percapita"] = gdp_model.predict(X_future)
            future["GDP_percapita"]     = np.exp(future["log_GDP_percapita"])

            future["trade_gdp"] = trade_model.predict(X_future)

            # update the group with future projections
            group.update(future)

        results.append(group)

    # Re-assemble
    df_projected = pd.concat(results).reset_index(drop=True)
    return df_projected
