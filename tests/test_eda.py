# tests/test_eda.py

import pytest
import os
from src.eda import load_dataset, check_missing_values, clean_data, perform_eda

#
data_path = 'data/Bank.csv'

def test_load_dataset():
    assert os.path.exists(data_path), "Dataset file does not exist."
    df = load_dataset(data_path)
    assert df.shape[0] > 0, "Dataset is empty."
    assert df.shape[1] > 0, "Dataset has no columns."

def test_check_missing_values():
    df = load_dataset(data_path)
    assert check_missing_values(df), "Dataset contains missing values."



#

def test_clean_data():
    df = load_dataset(data_path)
    clean_df = clean_data(df)
    assert clean_df.isnull().sum().sum() == 0, "There are still missing values after cleaning."

#

def test_perform_eda():
    df = load_dataset(data_path)
    summary_stats = perform_eda(df)
    assert not summary_stats.empty, "Summary statistics not generated properly."
    assert os.path.exists('data/eda_histograms.png'), "Histogram plots not saved."


































































# import pytest
# import pandas as pd
# import matplotlib.pyplot as plt
# from src.eda import load_data, check_missing_values, generate_summary_statistics, visualize_distributions


# def test_load_data():
#     df = load_data('data/bank_churn.csv')
#     assert isinstance(df, pd.DataFrame), "Data should be loaded into a pandas DataFrame"
#     assert not df.empty, "DataFrame should not be empty"

# def test_missing_values():
#     df = load_data('data/bank_churn.csv')
#     missing = df.isnull().sum()
#     assert missing.sum() == 0, "There should be no missing values in the dataset"

# def test_summary_statistics():
#     df = load_data('data/bank_churn.csv')
#     summary = df.describe()
#     assert 'age' in summary.columns, "Summary statistics should include 'Age'"
#     assert 'balance' in summary.columns, "Summary statistics should include 'Balance'"

# def test_visualizations():
#     df = load_data('data/bank_churn.csv')
#     # Since visualize_distributions() shows plots, we can check if it runs without errors
#     try:
#         visualize_distributions(df)
#     except Exception as e:
#         pytest.fail(f"Visualization failed with exception: {e}")
