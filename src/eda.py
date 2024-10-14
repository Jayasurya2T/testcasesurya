# Task 1: Load the Dataset
# Points: 5

import pandas as pd

def load_dataset(path):
    """Load the dataset from the given path."""
    df = pd.read_csv(path)
    return df

def check_missing_values(df):
    """Check if the dataset has any missing values."""
    return df.isnull().sum().sum() == 0

#Task 2: Cleaning DATA 
# Points: 5

def clean_data(df):
    """Clean the dataset by handling missing values, if any."""
    df.dropna(inplace=True)  # Drop rows with missing values (for simplicity)
    return df

#Task 3: Exploratory Data Analysis (EDA)
# Points: 5

# src/eda.py

import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    """Perform basic EDA, generate plots and summary statistics."""
    summary_stats = df.describe()
    
    # Visualize key variables
    df.hist(['Age', 'Balance', 'CreditScore', 'EstimatedSalary'], figsize=(10, 8))
    plt.savefig('data/eda_histograms.png')
    
    return summary_stats


if __name__ == "__main__":
    main()
