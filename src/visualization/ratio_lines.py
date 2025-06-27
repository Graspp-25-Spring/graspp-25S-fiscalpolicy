import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

def plot_dependency_ratio_lines(df_selected):
    # drop NAs etc
    df = df_selected.dropna(subset=['Dependency_Ratio_Old']).copy()

    # create fig & ax
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.set(style="whitegrid")

    for country in df['Country_Name'].unique():
        subset = df[df['Country_Name'] == country]
        ax.plot(subset['Year'],
                subset['Dependency_Ratio_Old'],
                label=country,
                linewidth=2)

        # annotate last point with flag + text …
        last = subset.sort_values('Year').iloc[-1]
        x, y = last['Year'], last['Dependency_Ratio_Old']
        iso3 = last['ISO3']
        flag_path = f"../references/flags/{iso3}.png"
        if os.path.exists(flag_path):
            img = Image.open(flag_path)
            zoom = 0.02
            imagebox = OffsetImage(img, zoom=zoom)
            ab = AnnotationBbox(imagebox,
                                (x+1, y),
                                frameon=False,
                                box_alignment=(0,0.5))
            ax.add_artist(ab)
        ax.text(x+4, y, country, va='center', fontsize=7)

    # labels, vertical line, grid, layout …
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Old-Age Dependency Ratio (%)", fontsize=12)
    ax.set_xlim(df['Year'].min(), df['Year'].max()+10)
    ax.axvline(2023, color='gray', linestyle='--', linewidth=1, alpha=0.6)
    ax.text(2023+0.5, ax.get_ylim()[1]-5, '2023',
            color='gray', fontsize=8)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.xaxis.grid(False)
    fig.tight_layout()

    # **NO** plt.show() here (or if you want, after saving outside)
    return fig

