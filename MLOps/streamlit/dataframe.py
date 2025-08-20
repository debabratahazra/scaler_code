import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

def open_dataframe():
    st.title("DataFrame Example")
    st.header("Displaying a DataFrame with Streamlit")

    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': np.random.rand(10),
        'B': np.random.rand(10),
        'C': np.random.rand(10)
    })

    # Display the DataFrame
    st.write("Here is a sample DataFrame:")
    st.dataframe(df)

    # Display the DataFrame as a table
    st.write("Here is the same DataFrame as a table:")
    st.table(df)

    # Display a chart using Altair
    chart = alt.Chart(df).mark_bar().encode(
        x='A',
        y='B',
        color='C'
    )
    
    st.altair_chart(chart, use_container_width=True)
