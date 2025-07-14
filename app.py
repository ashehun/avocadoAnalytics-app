import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go
# Load and preprocess data
data = (
    pd.read_csv("avocado.csv")
    .query("type == 'organic' and region == 'Atlanta'")
    .assign(Date=lambda df: pd.to_datetime(df["Date"], errors="coerce"))
    .sort_values(by="Date")
)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado Analytics: Understand Your Avocados!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(
                    children="Avocado Analytics", className="header-title"
                ),
                html.P(
                    children=(
                        "Analyze the behavior of avocado prices and the number"
                        " of avocados sold in the US between 2015 and 2018"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "bar",
                                    "hovertemplate": (
                                        "$%{y:.2f}<extra></extra>"
                                    ),
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Average Price of Avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17b897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        figure=go.Figure(
                            data=go.Scatter(
                                x=data["Date"],
                                y=data["AveragePrice"],
                                fill="tozeroy",  # ← makes it an area chart
                                mode="lines",
                                name="Average Price"
                            ),
                            layout=go.Layout(
                                title="Average Price (Area Chart)",
                                xaxis_title="Date",
                                yaxis_title="Average Price"
                            )
                        )
                    ),
##                    dcc.Graph(
##                        id="volume-chart",
##                        config={"displayModeBar": False},
##                        figure={
##                            "data": [
##                                {
##                                    "x": data["Date"],
##                                    "y": data["Total Volume"],
##                                    "type": "bar",
##                                },
##                            ],
##                            "layout": {
##                                "title": {
##                                    "text": "Avocados Sold",
##                                    "x": 0.05,
##                                    "xanchor": "left",
##                                },
##                                "xaxis": {"fixedrange": True},
##                                "yaxis": {"fixedrange": True},
##                                "colorway": ["#E12D39"],
##                            },
##                        },
##                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


##import pandas as pd
##from dash import Dash, dcc, html
##
### Load and preprocess data
##data = (
##    pd.read_csv("avocado.csv")
##    .query("type == 'organic' and region == 'Atlanta'")
##    .assign(Date=lambda df: pd.to_datetime(df["Date"], errors="coerce"))
##    .sort_values(by="Date")
##)
##
### Initialize Dash app
##app = Dash(__name__)
##app.title = "Avocado Analytics"
##
### Define layout
##app.layout = html.Div(
##    children=[
##        html.H1(children="Avocado Analytics Test on Dash"),
##        html.H4(
##            children=(
##                "Analyze the behavior of avocado prices and the number "
##                "of avocados sold in the US between 2015 and 2018"
##            )
##        ),
##
##        dcc.Graph(
##    id="price-chart",
##    figure={
##        "data": [
##            {
##                "x": data["Date"],
##                "y": data["AveragePrice"],
##                "type": "line",
##                "name": "Average Price",
##            },
##        ],
##        "layout": {
##            "title": {"text": "Average Price of Avocados", "x": 0.5},
##            "xaxis": {"title": {"text": "Date"}},
##            "yaxis": {"title": {"text": "Average Price of Avocado"}},
##        },
##    },
##),
##
##
##        dcc.Graph(
##    id="volume-chart",
##    figure={
##        "data": [
##            {
##                "x": data["Date"],
##                "y": data["Total Volume"],
##                "type": "line",
##                "name": "Total Volume",
##            },
##        ],
##        "layout": {
##            "title": {"text": "Avocados Sold", "x": 0.5},
##            "xaxis": {"title": {"text": "Date"}},
##            "yaxis": {"title": {"text": "Total Volume of Avocados"}},
##        },
##    },
##),
##
##    ],
##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
##
####    style={
####        "backgroundColor": "#90EE90",
####        "color": "#003366",
####        "fontWeight": "bold",
####        "textAlign": "center",
####    }
##)

##app.layout = html.Div(
##    children=[
##        html.H1(children="Avocado Analytics Test on Dash"),
##        html.H4(
##            children=
##                "Analyze the behavior of avocado prices and the number"
##                " of avocados sold in the US between 2015 and 2018"
##        ),
##        
##        dcc.Graph(
####            id="price-chart",
##            figure={
##                "data": [
##                    {
##                        "x": data["Date"],
##                        "y": data["AveragePrice"],
##                        "type": "lines",
##                    },
##                ],
##                "layout": {"title": "Average Price of Avocados"},
##            },
##        ),
##        dcc.Graph(
##            figure={
##                "data": [
##                    {
##                        "x": data["Date"],
##                        "y": data["Total Volume"],
##                        "type": "lines",
##                        "name": "Price"
##                    },
##                ],
##                "layout": {"title": "Avocados Sold"},
##            },
##        ),
##    ],
##    style={"backgroundColor":"#90EE90", "color": "#003366", "font-weight": "bold", "textAlign":"Center"}
#####000000, #003366, #222222, #333333    
##)
##app.layout = html.Div([
##    html.H1("Avocado Analytics"),
##    html.P("Analyze avocado prices and volumes in Albany (2015–2018)."),
##
##    dcc.Graph(
##        id="price-chart",
##        figure={
##            "data": [
##                {"x": data["Date"], "y": data["AveragePrice"], "type": "line", "name": "Price"},
##            ],
##            "layout": {"title": "Average Price of Avocados (Albany)"}
##        },
##    ),
##
##    dcc.Graph(
##        id="volume-chart",
##        figure={
##            "data": [
##                {"x": data["Date"], "y": data["Total Volume"], "type": "line", "name": "Volume"},
##            ],
##            "layout": {"title": "Total Avocados Sold (Albany)"}
##        },
##    ),
##])

# Run server
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
