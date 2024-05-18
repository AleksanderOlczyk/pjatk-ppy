import pandas as pd
import numpy as np
from collections import Counter

# Z4
data = pd.read_csv('loty.csv', sep='\t')
print("Pierwsze 5 wierszy danych:")
print(data.head())

print(f'Liczba danych przed operacjami: {data.shape}')
data.drop(columns=['Date', 'Location'], inplace=True)
data.dropna(inplace=True)

print(f'Liczba danych po operacjach usuwania: {data.shape}')
print("30 pierwszych wierszy po operacjach usuwania:")
print(data.head(30))

data['Weather'] = data['Weather'].astype('category').cat.codes
data['FlightCancelled'] = data['FlightCancelled'].map({'Yes': 1, 'No': 0})
print("30 pierwszych wierszy po zamianie wartości string na liczby:")
print(data.head(30))

# Podział zbioru na trzy podzbiory: train, valid oraz test
train_data = data.sample(frac=0.6, random_state=42)
remaining_data = data.drop(train_data.index)
valid_data = remaining_data.sample(frac=0.5, random_state=42)
test_data = remaining_data.drop(valid_data.index)

print(f"Liczba danych w zbiorze treningowym: {train_data.shape}")
print(f"Liczba danych w zbiorze walidacyjnym: {valid_data.shape}")
print(f"Liczba danych w zbiorze testowym: {test_data.shape}")

def min_max_scaling(column):
    return (column - column.min()) / (column.max() - column.min())

numeric_columns = ['Temperature', 'Humidity', 'WindSpeed']

for col in numeric_columns:
    train_data[col] = min_max_scaling(train_data[col])
    valid_data[col] = min_max_scaling(valid_data[col])
    test_data[col] = min_max_scaling(test_data[col])

print("Skalowanie zakończone.")

# Definiowanie X i y
X_train, y_train = train_data.drop(columns=['FlightCancelled']), train_data['FlightCancelled']
X_valid, y_valid = valid_data.drop(columns=['FlightCancelled']), valid_data['FlightCancelled']
X_test, y_test = test_data.drop(columns=['FlightCancelled']), test_data['FlightCancelled']

# ZD6 Implementacja
# Naiwny Klasyfikator Bayesa
class NaiveBayesClassifier:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.class_priors = y.value_counts() / len(y)
        self.feature_stats = {c: X[y == c].agg(['mean', 'var']).T for c in self.classes}

    def _calculate_likelihood(self, mean, var, x):
        exponent = np.exp(-((x - mean) ** 2) / (2 * var))
        return exponent / np.sqrt(2 * np.pi * var)

    def _calculate_posterior(self, x):
        posteriors = {}
        for c in self.classes:
            prior = np.log(self.class_priors[c])
            class_conditional = np.sum(np.log(self._calculate_likelihood(self.feature_stats[c]['mean'], self.feature_stats[c]['var'], x)))
            posteriors[c] = prior + class_conditional
        return max(posteriors, key=posteriors.get)

    def predict(self, X):
        return np.array([self._calculate_posterior(x) for x in X.itertuples(index=False)])


nb_model = NaiveBayesClassifier()
nb_model.fit(X_train, y_train)
nb_predictions = nb_model.predict(X_test)
nb_accuracy = (nb_predictions == y_test).mean()
print(f"Dokładność modelu Naive Bayes na zbiorze testowym: {nb_accuracy}")


# K-Najbliższych Sąsiadów (KNN)
class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X.reset_index(drop=True)
        self.y_train = y.reset_index(drop=True)

    def predict(self, X):
        predictions = []
        for row in X.itertuples(index=False):
            distances = []
            for train_row in self.X_train.itertuples(index=True):
                distance = np.linalg.norm(np.array(row) - np.array(train_row[1:]))
                distances.append((distance, self.y_train.iloc[train_row.Index]))
            nearest_neighbors = sorted(distances, key=lambda x: x[0])[:self.k]
            votes = [neighbor[1] for neighbor in nearest_neighbors]
            majority_vote = Counter(votes).most_common(1)[0][0]
            predictions.append(majority_vote)
        return np.array(predictions)


knn_model = KNNClassifier(k=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)
knn_accuracy = (knn_predictions == y_test).mean()
print(f"Dokładność modelu KNN na zbiorze testowym: {knn_accuracy}")

# Podsumowanie wyników
print("\nPodsumowanie wyników:")
print(f"Dokładność modelu Naive Bayes: {nb_accuracy}")
print(f"Dokładność modelu KNN: {knn_accuracy}")
