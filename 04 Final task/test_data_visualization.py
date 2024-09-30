import pandas as pd
import pytest
from data_visualization import load_data, filter_data, group_and_sort_data

# Define the specific platforms for testing
platforms_to_display = ['PS4', 'XOne', 'PC', 'WiiU']

@pytest.fixture
def setup_data():
    """Fixture to load and setup the DataFrame for testing."""
    # Use the load_data function from the program
    data = load_data('dataset.csv')
    return data

def test_load_data():
    """Test if data is loaded correctly."""
    data = load_data('dataset.csv')
    assert isinstance(data, pd.DataFrame), "Data should be loaded into a DataFrame"
    assert not data.empty, "Loaded DataFrame is empty"

def test_filter_platforms(setup_data):
    """Test if the DataFrame is correctly filtered by the specified platforms."""
    df_filtered = filter_data(setup_data, platforms_to_display)

    # Verify that only the platforms to display are in the filtered DataFrame
    assert set(df_filtered['platform'].unique()) == set(platforms_to_display), "Filtered DataFrame contains unexpected platforms"

def test_group_by_genre(setup_data):
    """Test if the group-by operation on 'platform' and 'genre' is correct."""
    df_filtered = filter_data(setup_data, platforms_to_display)
    final_df = group_and_sort_data(df_filtered)

    # Check if the DataFrame has the correct structure after group-by
    assert not final_df.empty, "Grouped DataFrame is empty"
    assert all(platform in platforms_to_display for platform in final_df.index), "DataFrame contains unexpected platforms"

def test_sorting_by_total_games(setup_data):
    """Test if the platforms are sorted correctly by the total game count."""
    df_filtered = filter_data(setup_data, platforms_to_display)
    platform_genre_count = group_and_sort_data(df_filtered)

    # Get sorted platforms by total games
    sorted_platforms = platform_genre_count.index.tolist()

    # Verify that the sorting is correctly done
    assert sorted_platforms == sorted(platform_genre_count.index, key=lambda x: platform_genre_count.loc[x].sum(), reverse=True), "Platforms are not sorted by total games correctly"
