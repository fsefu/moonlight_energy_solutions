from matplotlib import pyplot as plt
import streamlit as st
from src.data_loader import DataLoader
from src.data_processor import DataProcessor
from src.eda import EDA

class MainApp:
    def run(self):
        st.title("Solar Data Analysis Dashboard")

        # File uploader for the user to upload a CSV file
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            # Load data
            loader = DataLoader(uploaded_file)
            data = loader.load_data()

            # Process data
            processor = DataProcessor(data)
            clean_data = processor.clean_data()

            # Display raw data
            st.subheader("Raw Data")
            st.write(clean_data)

            # Perform and display EDA
            eda = EDA(clean_data)
            st.subheader("Correlation Heatmap")
            eda.plot_correlation_heatmap()
            st.pyplot(plt)

            st.subheader("Time Series of Solar Irradiance")
            eda.plot_time_series()
            st.pyplot(plt)

if __name__ == "__main__":
    app = MainApp()
    app.run()
