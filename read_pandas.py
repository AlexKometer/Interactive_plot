import pandas as pd
import plotly.express as px



def read_my_csv(path):
    df = pd.read_csv(path, sep="\t", header=None)
    df.columns = ["Messwerte in mV","Zeit in ms"]

    return df

def make_plot_ecg(df):
    # Creating a line plot using Plotly Express
    fig = px.line(df, x="Zeit in ms", y="Messwerte in mV")

    # Configuring the layout to include a range slider
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True,thickness=0.1),type='linear',fixedrange=False),yaxis=dict(fixedrange=True ))
    return fig

def make_plot_power(df2):
    fig = px.line (df2,x="Time in s",y=["PowerOriginal", "HeartRate"],color_discrete_sequence=["lightgray","royalblue"])

    HR_max = df2["HeartRate"].max ()
    zone1 = HR_max * 0.6
    zone2 = HR_max * 0.7
    zone3 = HR_max * 0.8
    zone4 = HR_max * 0.9

    df2["Zone1"] = df2["HeartRate"] < zone1
    df2["Zone2"] = (df2["HeartRate"] >= zone1) & (df2["HeartRate"] < zone2)
    df2["Zone3"] = (df2["HeartRate"] >= zone2) & (df2["HeartRate"] < zone3)
    df2["Zone4"] = (df2["HeartRate"] >= zone3) & (df2["HeartRate"] < zone4)
    df2["Zone5"] = df2["HeartRate"] >= zone4

    fig.add_hrect (y0=0, y1=zone1, fillcolor="lightgreen", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect (y0=zone1, y1=zone2, fillcolor="green", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect (y0=zone2, y1=zone3, fillcolor="yellow", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect (y0=zone3, y1=zone4, fillcolor="orange", opacity=0.5, layer="below", line_width=0)
    fig.add_hrect (y0=zone4, y1=HR_max, fillcolor="red", opacity=0.5, layer="below", line_width=0)

    return fig