import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Summary Statistics
def summary_statistics(df):
    return df.describe()

# Data Quality Check
def data_quality_check(df):
    missing_values = df.isnull().sum()
    outliers = df[(df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)]
    return missing_values, outliers

# Time Series Analysis
def time_series_analysis(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=df[['GHI', 'DNI', 'DHI', 'Tamb']])
    plt.title('Time Series Analysis of Solar Irradiance and Temperature')
    plt.show()

# Correlation Analysis
def correlation_analysis(df):
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Wind Analysis using Polar Plot
def wind_analysis(df):
    fig = px.scatter_polar(df, r="WS", theta="WD", color="WSstdev", size="WSgust",
                           color_continuous_scale=px.colors.sequential.Plasma,
                           title="Wind Speed and Direction Analysis")
    fig.show()

# Temperature and Humidity Analysis
def temp_humidity_analysis(df):
    sns.jointplot(x='RH', y='Tamb', data=df, kind='hex', cmap='coolwarm')
    plt.title('Temperature vs Relative Humidity')
    plt.show()

# Main Function
if __name__ == "__main__":
    df = load_data('data/solar_measurement_data.csv')
    
    # Summary Statistics
    print("Summary Statistics:")
    print(summary_statistics(df))
    
    # Data Quality Check
    print("\nData Quality Check:")
    missing_values, outliers = data_quality_check(df)
    print("Missing Values:\n", missing_values)
    print("Outliers:\n", outliers)
    
    # Time Series Analysis
    print("\nTime Series Analysis:")
    time_series_analysis(df)
    
    # Correlation Analysis
    print("\nCorrelation Analysis:")
    correlation_analysis(df)
    
    # Wind Analysis
    print("\nWind Analysis:")
    wind_analysis(df)
    
    # Temperature and Humidity Analysis
    print("\nTemperature and Humidity Analysis:")
    temp_humidity_analysis(df)
