# Add interaction features
import itertools

cat_features = ['ip', 'app', 'device', 'os', 'channel']
interactions = pd.DataFrame(index=clicks.index)

# Iterate through each pair of features, combine them into interaction features
for col1, col2 in itertools.combinations(cat_features, 2):
        new_col_name = '_'.join([col1, col2])

        # Convert to strings and combine
        new_values = clicks[col1].map(str) + "_" + clicks[col2].map(str)

        encoder = preprocessing.LabelEncoder()
        interactions[new_col_name] = encoder.fit_transform(new_values)


#

# Generating numerical features
def count_past_events(series):
    series = pd.Series(series.index, index=series)
    # Subtract 1 so the current event isn't counted
    past_events = series.rolling(time_window).count() - 1
    return past_events

def time_diff(series):
    """ Returns a series with the time since the last timestamp in seconds """
    return series.diff().dt.total_seconds()

def previous_attributions(series):
    """ Returns a series with the """
    # Subtracting raw values so I don't count the current event
    sums = series.expanding(min_periods=2).sum() - series
    return sums