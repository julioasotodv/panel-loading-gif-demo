import numpy as np
import pandas as pd
import time
import panel as pn
import hvplot.pandas
import holoviews as hv

pn.extension()
hv.extension("bokeh")


df = pd.DataFrame({"a": np.random.randn(100),
                   "b": np.random.randn(100)})

loading_gif = pn.pane.GIF("https://media1.tenor.com/images/713a3272124cc57ba9e9fb7f59e9ab3b/tenor.gif",
                          height=100,
                          embed=True)

button = pn.widgets.Button(name="Button!")
chart = df.hvplot(kind="scatter", x="a", y="b", title="Number of clicks to button: %s" % button.clicks)
column = pn.Column(button, chart)

def loading_and_update(*events):
    column[:] = [button, loading_gif]
    
    for event in events:
        if event.name == "clicks":
            number_clicks = event.new
            
    # Some busy working...
    for i in range(150000000):
        a=1
        
    # Re-generate chart and update:
    chart = df.hvplot(kind="scatter", x="a", y="b", title="Number of clicks to button: %s" % number_clicks)
    column[:] = [button, chart]
    
# Add callback to button
button.param.watch(loading_and_update, ["clicks"])

column.servable()


