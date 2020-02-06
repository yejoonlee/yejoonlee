# Univariate Feature Selection
from sklearn.feature_selection import SelectKBest, f_classif
feature_cols = clicks.columns.drop(['click_time', 'attributed_time', 'is_attributed'])
train, valid, test = get_data_splits(clicks)

# Create the selector, keeping 40 features
selector = SelectKBest(f_classif, k=40)

# Use the selector to retrieve the best features
X_new = selector.fit_transform(train[feature_cols], train['is_attributed'])

# Get back the kept features as a DataFrame with dropped columns as all 0s
selected_features = pd.DataFrame(selector.inverse_transform(X_new),
                                 index=train.index,
                                 columns=feature_cols)

# Find the columns that were dropped
dropped_columns = selected_features.columns[selected_features.var() == 0]

#

# Use L1 regularization for feature selection
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel


def select_features_l1(X, y):
    """ Return selected features using logistic regression with an L1 penalty """
    logistic = LogisticRegression(C=0.1, penalty="l1", random_state=7).fit(X, y)
    model = SelectFromModel(logistic, prefit=True)

    X_new = model.transform(X)

    # Get back the kept features as a DataFrame with dropped columns as all 0s
    selected_features = pd.DataFrame(model.inverse_transform(X_new),
                                     index=X.index,
                                     columns=X.columns)

    # Dropped columns have values of all 0s, keep other columns
    selected = selected_features.columns[selected_features.var() != 0]

    return selected