import pandas as pd
from scripts.eda import summary_statistics, correlation_analysis

# Load the cleaned dataset
df = pd.read_csv('data/clean-benin-malanville.csv')

# Summary Statistics
print("Final Summary Statistics:")
print(summary_statistics(df))

# Correlation Analysis
print("\nFinal Correlation Analysis:")
correlation_analysis(df)

# Strategy Recommendation
def recommend_strategy(df):
    # Example strategy: Identify high-potential regions based on GHI
    df['HighPotential'] = df['GHI'] > df['GHI'].quantile(0.75)
    regions = df.groupby('Region')['HighPotential'].mean().sort_values(ascending=False)
    return regions

print("\nStrategy Recommendation:")
print(recommend_strategy(df))
