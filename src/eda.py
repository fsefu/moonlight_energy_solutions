import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, data):
        self.data = data

    def plot_correlation_heatmap(self):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap of Solar Data')
        # Remove plt.show() since Streamlit handles the display
        # plt.show()

    def plot_time_series(self):
        plt.figure(figsize=(14, 8))
        plt.plot(self.data['Timestamp'], self.data['GHI'], label='GHI')
        plt.plot(self.data['Timestamp'], self.data['DNI'], label='DNI')
        plt.plot(self.data['Timestamp'], self.data['DHI'], label='DHI')
        plt.xlabel('Timestamp')
        plt.ylabel('Irradiance (W/m²)')
        plt.title('Time Series of Solar Irradiance')
        plt.legend()
        # Remove plt.show() since Streamlit handles the display
        # plt.show()
