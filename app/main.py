import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/clean_solar_measurement_data.csv')

# Dashboard
st.title("MoonLight Energy Solutions Dashboard")
st.markdown("## Solar Radiation Data Insights")

# Time Series Plot
st.markdown("### Time Series of Solar Irradiance")
fig = px.line(df, x='Timestamp', y=['GHI', 'DNI', 'DHI'], title="Time Series Analysis")
st.plotly_chart(fig)

# Correlation Heatmap
st.markdown("### Correlation Heatmap")
corr = df.corr()
fig = px.imshow(corr, text_auto=True, title="Correlation Analysis")
st.plotly_chart(fig)

# Wind Analysis
st.markdown("### Wind Speed and Direction")
fig = px.scatter_polar(df, r="WS", theta="WD", color="WSstdev", size="WSgust",
                       color_continuous_scale=px.colors.sequential.Plasma,
                       title="Wind Speed and Direction Analysis")
st.plotly_chart(fig)

st.markdown("### Strategy Recommendation")
high_potential_regions = df.groupby('Region')['GHI'].mean().sort_values(ascending=False)
st.write(high_potential_regions)

# Run the app with: streamlit run app/main.py
