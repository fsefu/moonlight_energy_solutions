class DataProcessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data.dropna(subset=['Timestamp'], inplace=True)
        numerical_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data[numerical_cols] = self.data[numerical_cols].fillna(self.data[numerical_cols].median())
        return self.data

    # Other processing methods can be added here
