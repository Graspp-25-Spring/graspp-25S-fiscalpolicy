import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.patches import Patch

# === Constants ===
FEMALE_COLOR = "#F64740"
MALE_COLOR = "#05B2DC"

# === Styling ===
def set_seaborn_style(font_family, background_color, grid_color, text_color):
    sns.set_style({
        "axes.facecolor": background_color,
        "figure.facecolor": background_color,
        "axes.labelcolor": text_color,
        "axes.edgecolor": grid_color,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": grid_color,
        "font.family": font_family,
        "text.color": text_color,
        "xtick.color": text_color,
        "ytick.color": text_color,
        "xtick.bottom": False,
        "xtick.top": False,
        "ytick.left": False,
        "ytick.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": True,
        "axes.spines.right": False,
        "axes.spines.top": False,
    })

# === Plotting Utilities ===
def create_x_labels(ax, xformat):
    if xformat == "billions":
        return ["{}B".format(round(abs(x / 1e9))) for x in ax.get_xticks()[1:-1]]
    elif xformat == "millions":
        return ["{}M".format(round(abs(x / 1e6))) for x in ax.get_xticks()[1:-1]]
    elif xformat == "thousands":
        return ["{}K".format(round(abs(x / 1e3))) for x in ax.get_xticks()[1:-1]]
    elif xformat == "percentage":
        return ["{}%".format(round(abs(x), 1)) for x in ax.get_xticks()[1:-1]]

def format_ticks(ax, xformat, xlim=(None, None)):
    ax.tick_params(axis="x", labelsize=12, pad=8)
    ax.tick_params(axis="y", labelsize=12)
    ax.set(ylabel=None, xlabel=None, xlim=xlim)
    plt.xticks(
        ticks=ax.get_xticks()[1:-1],
        labels=create_x_labels(ax, xformat)
    )

def add_legend(x, y, background_color): 
    patches = [
        Patch(color=MALE_COLOR, label="Male"),
        Patch(color=FEMALE_COLOR, label="Female")
    ]
    plt.legend(
        handles=patches,
        bbox_to_anchor=(x, y), loc='center',
        ncol=2, fontsize=15,
        handlelength=1, handleheight=0.4,
        edgecolor=background_color
    )

def create_image_from_figure(fig):
    plt.tight_layout()
    fig.canvas.draw()
    data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    data = data.reshape((fig.canvas.get_width_height()[::-1]) + (3,))
    plt.close()
    return Image.fromarray(data)

def add_padding_to_chart(chart, left, top, right, bottom, background):
    size = chart.size
    image = Image.new("RGB", (size[0] + left + right, size[1] + top + bottom), background)
    image.paste(chart, (left, top))
    return image

def create_age_distribution(female_df, male_df, country_code, year):
    df_f = female_df[female_df.country_code == country_code].loc[::-1]
    df_m = male_df[male_df.country_code == country_code].loc[::-1]
    
    ax = sns.barplot(y=df_m["indicator_name"], x=df_m[year] * -1, orient="h", color=MALE_COLOR)
    ax = sns.barplot(y=df_f["indicator_name"], x=df_f[year], orient="h", color=FEMALE_COLOR)
    
    return ax

def create_grid(figures, pad, ncols):
    nrows = int(len(figures) / ncols) + (len(figures) % ncols > 0)
    size = figures[0].size

    image = Image.new(
        "RGBA",
        (ncols * size[0] + (ncols - 1) * pad, nrows * size[1] + (nrows - 1) * pad),
        "#ffffff00"
    )

    for i, figure in enumerate(figures):
        col, row = i % ncols, i // ncols
        image.paste(figure, (col * (size[0] + pad), row * (size[1] + pad)))

    return image


def generate_country_figure(female_df, male_df, country_code, year, background_color, xformat="percentage", xlim=(-10, 10)):
    fig = plt.figure(figsize=(10, 8))

    ax = create_age_distribution(female_df, male_df, country_code, year)
    ax.set(xlim=xlim)

    format_ticks(ax, xformat=xformat)
    add_legend(x=0.5, y=1.09, background_color=background_color)

    country_name = female_df[female_df.country_code == country_code]["country_name"].iloc[0]
    region_title = country_name.title() if country_name.lower() != "world" else "the World"
    plt.title(f"Age Distribution for {region_title} in {year}", y=1.14, fontsize=20)

    image = create_image_from_figure(fig)
    image = add_padding_to_chart(image, 20, 20, 20, 5, background_color)

    return image
