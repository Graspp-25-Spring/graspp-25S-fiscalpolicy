import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

def plot_dependency_ratio_lines(df_selected):
    df_selected = df_selected.dropna(subset=['Dependency_Ratio_Old']).copy()

    plt.figure(figsize=(8, 5))
    sns.set(style="whitegrid")

    for country in df_selected['Country_Name'].unique():
        subset = df_selected[df_selected['Country_Name'] == country]
        plt.plot(subset['Year'], subset['Dependency_Ratio_Old'], label=country, linewidth=2)

        last_point = subset.sort_values('Year').iloc[-1]
        x, y = last_point['Year'], last_point['Dependency_Ratio_Old']

        iso3 = subset['ISO3'].iloc[0]
        flag_path = f"../references/flags/{iso3}.png"
        if os.path.exists(flag_path):
            img = Image.open(flag_path)
            zoom_factor = 0.02
            imagebox = OffsetImage(img, zoom=zoom_factor)
            ab = AnnotationBbox(imagebox, (x + 1, y), frameon=False, box_alignment=(0, 0.5))
            plt.gca().add_artist(ab)

        plt.text(x + 4, y, country, va='center', fontsize=7)

    plt.title("Old-Age Dependency Ratio Projection of Selected Countries", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Old-Age Dependency Ratio (%)", fontsize=12)
    plt.xlim(df_selected['Year'].min(), df_selected['Year'].max() + 10)
    plt.axvline(x=2023, color='gray', linestyle='--', linewidth=1, alpha=0.6)
    plt.text(2023 + 0.5, plt.ylim()[1] - 5, '2023', color='gray', fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.gca().xaxis.grid(False)
    plt.tight_layout()
    plt.show()
