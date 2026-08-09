import plotly.graph_objects as go
def score_gauge(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "AI Investment Score"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "bar": {
                    "color": "darkblue"
                },
                "steps": [
                    {
                        "range": [0, 50],
                        "color": "#ffb3b3"
                    },
                    {
                        "range": [50, 70],
                        "color": "#ffe680"
                    },
                    {
                        "range": [70, 85],
                        "color": "#b3ffb3"
                    },
                    {
                        "range": [85, 100],
                        "color": "#66ff66"
                    }
                ]
            }
        )
    )
    fig.update_layout(
        height=350
    )
    return fig