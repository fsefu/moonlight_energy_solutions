import pandas as pd

# Cleaning Data
def clean_data(df):
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    # Handle negative values where not applicable
    df.loc[df['GHI'] < 0, 'GHI'] = 0
    df.loc[df['DNI'] < 0, 'DNI'] = 0
    df.loc[df['DHI'] < 0, 'DHI'] = 0
    
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/solar_measurement_data.csv')
    clean_df = clean_data(df)
    clean_df.to_csv('data/clean_solar_measurement_data.csv', index=False)
