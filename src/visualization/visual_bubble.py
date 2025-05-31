# src/Import_and_Cleaning/visualize_bubbles.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_dependency_bubbles(change_df):
    # Quadrants
    bottom_left = change_df[(change_df['Delta_Old'] < 0) & (change_df['Delta_Young'] < 0)]
    top_right = change_df[(change_df['Delta_Old'] > 0) & (change_df['Delta_Young'] > 0)]
    top_left = change_df[(change_df['Delta_Old'] > 0) & (change_df['Delta_Young'] < 0)]
    top5_top_left = top_left.sort_values(by='Delta_Old', ascending=False).head(5)

    # Plot
    plt.figure(figsize=(7, 7))
    sns.scatterplot(
        data=change_df,
        x='Delta_Young',
        y='Delta_Old',
        size='Log_Population',
        sizes=(20, 300),
        alpha=0.6,
        legend=False
    )
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(0, color='gray', linestyle='--')
    plt.xlabel("Δ Young Dependency Ratio (2050 - 1960)", fontsize=12)
    plt.ylabel("Δ Old Dependency Ratio (2050 - 1960)", fontsize=12)
    plt.title("Demographic Shifts by Country (Bubble Size = log Population 2050)", fontsize=14)

    # Label offset
    offset = -3
    for _, row in bottom_left.iterrows():
        plt.text(row['Delta_Young'], row['Delta_Old'] + offset, row['Country'], fontsize=6, color='blue', ha='center')
    for _, row in top_right.iterrows():
        plt.text(row['Delta_Young'], row['Delta_Old'] + offset, row['Country'], fontsize=6, color='green', ha='center')
    for _, row in top5_top_left.iterrows():
        plt.text(row['Delta_Young'], row['Delta_Old'] + offset, row['Country'], fontsize=6, color='red', ha='center')

    plt.grid(True)
    plt.show()
