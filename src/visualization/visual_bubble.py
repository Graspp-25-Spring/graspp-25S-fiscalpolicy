# src/Import_and_Cleaning/visualize_bubbles.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_dependency_bubbles(change_df):
    # ─── Style setup ─────────────────────────────────────────────
    # use a clean white background with no grid
    sns.set_style("white")

    # ─── Identify quadrants ─────────────────────────────────────
    bottom_left  = change_df[(change_df['Delta_Old']   < 0) & (change_df['Delta_Young'] < 0)]
    top_right    = change_df[(change_df['Delta_Old']   > 0) & (change_df['Delta_Young'] > 0)]
    top_left     = change_df[(change_df['Delta_Old']   > 0) & (change_df['Delta_Young'] < 0)]
    top5_top_left = top_left.sort_values(by='Delta_Old', ascending=False).head(5)

    # ─── Plot ─────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=change_df,
        x='Delta_Young',
        y='Delta_Old',
        size='Log_Population',
        sizes=(20, 300),
        alpha=0.6,
        legend=False,
        ax=ax
    )

    # zero lines
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax.axvline(0, color='gray', linestyle='--', linewidth=1)

    # labels
    ax.set_xlabel("Δ Young Dependency Ratio (2050 - 1960)", fontsize=12)
    ax.set_ylabel("Δ Old Dependency Ratio   (2050 - 1960)", fontsize=12)
    ax.set_title("Demographic Shifts by Country (Bubble Size = log Population 2050)", fontsize=14)

    # ─── Annotations ─────────────────────────────────────────────
    offset = -3
    for _, row in bottom_left.iterrows():
        ax.text(row['Delta_Young'], row['Delta_Old'] + offset,
                row['Country'], fontsize=6, color='blue', ha='center')
    for _, row in top_right.iterrows():
        ax.text(row['Delta_Young'], row['Delta_Old'] + offset,
                row['Country'], fontsize=6, color='green', ha='center')
    for _, row in top5_top_left.iterrows():
        ax.text(row['Delta_Young'], row['Delta_Old'] + offset,
                row['Country'], fontsize=6, color='red', ha='center')

    # ─── Remove grid ──────────────────────────────────────────────
    ax.grid(False)

    # optional: remove top/right spines for extra clean look
    sns.despine(ax=ax)

    plt.show()
