import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output

# === Data loading & prep ===
df = pd.read_csv("../data/processed/hep_hee_results_with_region.csv")
df = df[df["income_level"].notnull()]
df["Year"] = df["Year"].astype(int)
df = df.sort_values("Year")
df["Year_str"] = df["Year"].astype(str)

df_avg = (
    df[df["Year"].between(2000, 2022)]
      .groupby(["ISO3", "income_level"])[["HEP", "HEE", "HEP_Health", "HEE_Health", "HEP_Edu", "HEE_Edu"]]
      .mean()
      .reset_index()
)
df_avg["text"] = df_avg["ISO3"] + " (avg)"

available_countries = sorted(df["ISO3"].unique())
available_income_levels = sorted(df["income_level"].unique())

# === Figure factories ===
def make_animated_scatter(dff, dff_avg, x_col, y_col, title, avg_x, avg_y, show_avg):
    fig = px.scatter(
        dff, x=x_col, y=y_col, color="income_level", text="ISO3",
        animation_frame="Year_str", range_x=[0,2], range_y=[0,2],
        labels={x_col: f"Performance ({x_col})", y_col: f"Efficiency ({y_col})"},
        title=title, width=950, height=600
    )
    fig.update_traces(marker=dict(size=10), textposition="top center")

    if show_avg:
        fig.add_trace(go.Scatter(
            x=dff_avg[avg_x], y=dff_avg[avg_y], mode="markers+text",
            text=dff_avg["text"], textposition="bottom center",
            marker=dict(size=9, symbol="diamond", opacity=0.4),
            name="2000–2022 Avg"
        ))

    fig.add_shape(
        type="line", x0=0, y0=0, x1=2, y1=2,
        line=dict(dash="dash", color="gray")
    )
    return fig

def make_static_avg_scatter(dff_avg, x_col, y_col):
    fig = px.scatter(
        dff_avg, x=x_col, y=y_col, color="income_level", text="ISO3",
        range_x=[0,1.5], range_y=[0,2.5],
        labels={x_col: f"Performance ({x_col})", y_col: f"Efficiency ({y_col})"},
        width=950, height=600
    )
    fig.update_traces(marker=dict(size=10), textposition="top center")
    return fig

def make_bar_chart(dff_avg):
    df_sorted = dff_avg.sort_values("HEP", ascending=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_sorted["HEP"], y=df_sorted["ISO3"], orientation='h', name="Avg HEP", marker_color="red"
    ))
    fig.add_trace(go.Bar(
        x=df_sorted["HEE"], y=df_sorted["ISO3"], orientation='h', name="Avg HEE", marker_color="orange"
    ))
    fig.update_layout(
        barmode='group',
        title_text="Avg HEP vs HEE index by Country (2000–2022)",
        xaxis_title="Index Value",
        yaxis_title="Country",
        yaxis=dict(autorange="reversed"),
        height=1000,
        margin=dict(l=100, r=20, t=50, b=50)
    )
    return fig

# === Public API ===
def get_figures(
    selected_countries: list[str] = None,
    selected_income_levels: list[str] = None,
    show_avg: bool = True
):
    # defaults
    if selected_countries is None or "ALL" in selected_countries:
        selected_countries = available_countries
    if selected_income_levels is None:
        selected_income_levels = available_income_levels

    dff = df[df["ISO3"].isin(selected_countries) & df["income_level"].isin(selected_income_levels)]
    dff_avg = df_avg[df_avg["ISO3"].isin(selected_countries) & df_avg["income_level"].isin(selected_income_levels)]

    # build each figure
    fig_main   = make_animated_scatter(dff, dff_avg, "HEP", "HEE", "HEP vs HEE Index (Overall)",     "HEP",       "HEE",       show_avg)
    fig_health = make_animated_scatter(dff, dff_avg, "HEP_Health", "HEE_Health", "HEP vs HEE (Health Only)", "HEP_Health", "HEE_Health", show_avg)
    fig_edu    = make_animated_scatter(dff, dff_avg, "HEP_Edu",    "HEE_Edu",    "HEP vs HEE (Education Only)", "HEP_Edu", "HEE_Edu",    show_avg)

    fig_avg_main   = make_static_avg_scatter(dff_avg, "HEP",       "HEE")
    fig_avg_health = make_static_avg_scatter(dff_avg, "HEP_Health","HEE_Health")
    fig_avg_edu    = make_static_avg_scatter(dff_avg, "HEP_Edu",   "HEE_Edu")

    fig_bar = make_bar_chart(dff_avg)

    return fig_main, fig_health, fig_edu, fig_avg_main, fig_avg_health, fig_avg_edu, fig_bar

def create_app():
    app = dash.Dash(__name__)
    app.title = "HEP vs HEE Dashboard"

    # same layout you already had…
    app.layout = html.Div([...])

    @app.callback(
        Output("animated-scatter-main", "figure"),
        Output("animated-scatter-health", "figure"),
        Output("animated-scatter-edu", "figure"),
        Output("avg-scatter-main", "figure"),
        Output("avg-scatter-health", "figure"),
        Output("avg-scatter-edu", "figure"),
        Output("bar-chart-hep-hee", "figure"),
        Input("country-dropdown", "value"),
        Input("income-dropdown", "value"),
        Input("avg-toggle", "value")
    )
    def _update(countries, incomes, toggles):
        return get_figures(countries, incomes, "show_avg" in toggles)

    return app

if __name__ == "__main__":
    create_app().run_server(debug=True)
