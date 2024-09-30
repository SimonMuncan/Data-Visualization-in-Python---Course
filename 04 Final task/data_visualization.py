import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    data = pd.read_csv(file_path, engine='python')
    return data

def filter_data(data, platforms):
    """Filter the DataFrame to include only the specified platforms."""
    return data[data['platform'].isin(platforms)]

def group_and_sort_data(df_filtered):
    """Group by platform and genre, count occurrences, and sort by total games."""
    # Group by platform and genre, then count the occurrences
    platform_genre_count = df_filtered.groupby(['platform', 'genre']).size().unstack(fill_value=0)

    # Sum across genres to get total game count per platform
    platform_genre_count['Total Games'] = platform_genre_count.sum(axis=1)

    # Sort platforms by total game count in descending order
    sorted_df = platform_genre_count.sort_values('Total Games', ascending=False)

    # Drop the 'Total Games' column (we don't need it in the plot)
    final_df = sorted_df.drop(columns=['Total Games'])
    return final_df

def plot_data(final_df):
    """Create the grouped bar chart with the given DataFrame."""
    ax = final_df.plot(kind='bar', stacked=False, figsize=(10, 5), zorder=3)

    # Set background, no border line
    ax.set_facecolor('lightgray')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(axis='both', which='both', length=0) 

    # Set title, labels, legend...
    plt.title('Number of games per platform')
    plt.xlabel('platform')
    plt.ylabel('count')
    plt.xticks(rotation=0)
    plt.legend(title='genre', loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    plt.tight_layout() 
    plt.grid(axis='y', color='white', which='both', linewidth=0.5, alpha=0.7, zorder=0)

    # Show plot
    plt.show()

def main(data_file):
    """Main function to execute the complete workflow."""
    platforms_to_display = ['PS4', 'XOne', 'PC', 'WiiU']

    # Load, filter, and process data
    data = load_data(data_file)
    df_filtered = filter_data(data, platforms_to_display)
    final_df = group_and_sort_data(df_filtered)

    # Plot the final data
    plot_data(final_df)

# If the script is run directly, execute main()
if __name__ == '__main__':
    main('04 Final task/dataset.csv')