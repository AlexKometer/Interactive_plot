import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot_ecg, make_plot_power
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

df2 = pd.read_csv("data/activities/activity.csv")

t_end = len(df2["PowerOriginal"])

df2["Time in s"] = np.arange(0, t_end)
HR_max = df2["HeartRate"].max ()



tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot_ecg(df)

    st.plotly_chart(fig)

with tab2:
    st.subheader ("Interaktiver Plot")
    st.header("Power- & Heart-Data")
    fig = make_plot_power(df2)
    st.plotly_chart (fig)



