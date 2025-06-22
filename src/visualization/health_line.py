import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

def get_health_data(
    path="../data/interim/merged_data_with_health.csv",
    iso_codes=None
):
    if iso_codes is None:
        iso_codes = [
            "USA","KOR","JPN","CAN","BRA","CHL",
            "CHN","GBR","THA","IDN","IND","RUS","VNM","MNG"
        ]

    name_map = {
        "USA":"United States","KOR":"South Korea","JPN":"Japan",
        "CAN":"Canada","BRA":"Brazil","CHL":"Chile","CHN":"China",
        "GBR":"United Kingdom","THA":"Thailand","IDN":"Indonesia","IND":"India",
        "RUS":"Russia","VNM":"Vietnam","MNG":"Mongolia"
    }

    df = pd.read_csv(path)
    df = df[df["ISO3"].isin(iso_codes)].copy()
    df["Country_Name"] = df["ISO3"].map(name_map)
    df = df[(df["Year"] >= 2000) & (df["Year"] <= 2050)]
    return df


def plot_health_lines(df):
    plt.figure(figsize=(12, 7))
    #sns.set(style="whitegrid")

    # 1) shade COVID years 2020–2021
    plt.axvspan(2020, 2021, color="gray", alpha=0.25)
    # optional label
    ymax = plt.ylim()[1]
    plt.text(
        2020.5, ymax * 0.98,
        "COVID period",
        ha="center",
        va="top",
        color="gray",
        fontsize=9,
        fontstyle="italic"
    )

    # 2) plot each country’s timeseries
    for country in df["Country_Name"].unique():
        subset = df[df["Country_Name"] == country]
        plt.plot(
            subset["Year"],
            subset["Health_Expenditure"],
            linewidth=1.8,
            alpha=0.8
        )

        # flag + name at final year
        last = subset.sort_values("Year").iloc[-1]
        x, y = last["Year"], last["Health_Expenditure"]
        iso = last["ISO3"]

        flag_path = f"../references/flags/{iso}.png"
        if os.path.exists(flag_path):
            img = Image.open(flag_path)
            zoom = 0.02
            im = OffsetImage(img, zoom=zoom)
            ab = AnnotationBbox(
                im, (x, y),
                frameon=False,
                box_alignment=(0, 0.5)
            )
            plt.gca().add_artist(ab)

        plt.text(
            x + 1, y,
            country,
            va="center",
            fontsize=9
        )

    # 3) mark projection start
    plt.axvline(2023, color="gray", linestyle="--", linewidth=1)
    plt.text(
        2023.5,
        ymax * 0.92,
        "Projection →",
        color="gray",
        fontsize=9
    )

    # 4) labels
    plt.title("Health Expenditure (% of GDP) 2000–2050", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Health Expenditure (% GDP)", fontsize=12)

    # 5) no legend
    # plt.legend().remove()

    plt.tight_layout()
    plt.show()