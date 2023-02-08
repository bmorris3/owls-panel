import panel as pn



def get_plot(theme="default"):
    """Returns a Vega-lite plot"""
    vegalite = {
        "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
        "data": {"url": "https://raw.githubusercontent.com/vega/vega/master/docs/data/barley.json"},
        "mark": {"type": "bar", "tooltip": True},
        "width": "container",
        "height": "container",
        "encoding": {
            "x": {"aggregate": "sum", "field": "yield", "type": "quantitative"},
            "y": {"field": "variety", "type": "nominal"},
            "color": {"field": "site", "type": "nominal"},
        },
    }

    if theme == "dark":
        vegalite["config"] = {
            "background": "#333",
            "title": {"color": "#fff"},
            "style": {"guide-label": {"fill": "#fff"}, "guide-title": {"fill": "#fff"}},
            "axis": {"domainColor": "#fff", "gridColor": "#888", "tickColor": "#fff"},
        }
    return vegalite


plot = get_plot()
pn.pane.Vega(plot, height=700, sizing_mode="stretch_both").servable()
