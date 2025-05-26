import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def project_log_gdp(input_path="../data/interim/merged_data.csv"):
    # Load data
    df = pd.read_csv(input_path)

    # Create log of GDP per capita
    df["log_GDP_percapita"] = np.log(df["GDP_percapita"])

    # Placeholder to collect all updated rows
    results = []

    # Loop by country
    for country, group in df.groupby("Country"):
        group = group.sort_values("Year").copy()

        # Use historical data up to 2022 with valid GDP
        train = group[(group["Year"] < 2023) & (group["log_GDP_percapita"].notna())]

        if len(train) >= 5:  # Ensure enough data points
            X = train[["Year"]]
            y = train["log_GDP_percapita"]

            model = LinearRegression().fit(X, y)

            group_future = group[group["Year"] >= 2023].copy()
            X_future = group_future[["Year"]]

            # Predict future log GDP
            y_pred_log = model.predict(X_future)

            group_future["log_GDP_percapita"] = y_pred_log
            group_future["GDP_percapita"] = np.exp(y_pred_log)

            # Update future rows in the group
            group.update(group_future)

        results.append(group)

    # Combine all country data back into one DataFrame
    df_projected = pd.concat(results).reset_index(drop=True)
    return df_projected
