import numpy as np
from collections import defaultdict


def calculate_class_probs(y):
    """
    Calculate prior probabilities for each class
    Args:
        y: List of class labels
    Returns:
        Dictionary of class probabilities and class counts
    """
    class_counts = {}
    for label in y:
        class_counts[label] = class_counts.get(label, 0) + 1

    # Calculate P(class)
    n_samples = len(y)
    class_probs = {label: count / n_samples for label, count in class_counts.items()}

    return class_probs, class_counts


def calculate_feature_probs(X, y, class_counts):
    """
    Calculate likelihood probabilities for features
    Args:
        X: List of feature lists
        y: List of class labels
        class_counts: Dictionary of class counts
    Returns:
        Dictionary of feature probabilities per class
    """
    # Count feature occurrences per class
    feature_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for i in range(len(X)):
        current_class = y[i]
        for feature_idx, feature_value in enumerate(X[i]):
            feature_counts[feature_idx][current_class][feature_value] += 1

    # Calculate P(feature|class)
    feature_probs = defaultdict(lambda: defaultdict(dict))
    for feature_idx in feature_counts:
        for class_label in class_counts:
            total_class_samples = class_counts[class_label]
            for feature_value in feature_counts[feature_idx][class_label]:
                count = feature_counts[feature_idx][class_label][feature_value]
                prob = count / total_class_samples
                feature_probs[feature_idx][class_label][feature_value] = prob

    return feature_probs


def train_naive_bayes(X, y):
    """
    Train the Naive Bayes model
    Args:
        X: List of feature lists
        y: List of class labels
    Returns:
        Tuple of class and feature probabilities
    """
    class_probs, class_counts = calculate_class_probs(y)
    feature_probs = calculate_feature_probs(X, y, class_counts)

    return class_probs, feature_probs


def predict_naive_bayes(X, class_probs, feature_probs):
    """
    Make predictions using Naive Bayes
    Args:
        X: List of feature lists to predict
        class_probs: Dictionary of class probabilities
        feature_probs: Dictionary of feature probabilities
    Returns:
        List of predicted classes
    """
    predictions = []

    for sample in X:
        # Calculate probability for each class
        class_scores = {}
        for class_label in class_probs:
            # Start with log prior probability
            score = np.log(class_probs[class_label])

            # Add log likelihood probabilities
            for feature_idx, feature_value in enumerate(sample):
                # Add small value for Laplace smoothing
                probability = feature_probs[feature_idx][class_label].get(
                    feature_value, 1e-10)
                score += np.log(probability)

            class_scores[class_label] = score

        # Select class with highest probability
        predicted_class = max(class_scores, key=class_scores.get)
        predictions.append(predicted_class)

    return predictions


# Example usage
if __name__ == "__main__":
    # Sample dataset: Weather conditions and decision to play tennis
    # Features: [Outlook, Temperature, Humidity, Windy]
    X_train = [
        ['Sunny', 'Hot', 'High', 'False'],
        ['Sunny', 'Hot', 'High', 'True'],
        ['Overcast', 'Hot', 'High', 'False'],
        ['Rain', 'Mild', 'High', 'False'],
        ['Rain', 'Cool', 'Normal', 'False'],
        ['Rain', 'Cool', 'Normal', 'True'],
    ]

    y_train = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No']

    # Train the model
    class_probs, feature_probs = train_naive_bayes(X_train, y_train)

    # Make predictions
    X_test = [['Sunny', 'Cool', 'High', 'True']]
    predictions = predict_naive_bayes(X_test, class_probs, feature_probs)
    print(f"Prediction for {X_test[0]}: {predictions[0]}")