"""
Comprehensive Iris Dataset Classification - All 9 Problem Statements
Plug-and-play sklearn code for Decision Trees, Logistic Regression, 
Ensemble Methods, and PCA
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (BaggingClassifier, RandomForestClassifier,
                              GradientBoostingClassifier, AdaBoostClassifier)
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')


# ============================================================================
# LOAD AND UNDERSTAND DATASET
# ============================================================================
def load_and_explore_data():
    """Load Iris dataset and perform basic exploration"""
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['species'] = df['target'].map({0: iris.target_names[0],
                                      1: iris.target_names[1],
                                      2: iris.target_names[2]})

    print("=" * 80)
    print("IRIS DATASET OVERVIEW")
    print("=" * 80)
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nFeatures: {iris.feature_names}")
    print(f"\nTarget Classes: {iris.target_names}")
    print(f"\nClass Distribution:\n{df['species'].value_counts()}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nDataset Info:")
    print(df.info())
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nStatistical Summary:\n{df.describe()}")
    print("\n" + "=" * 80 + "\n")

    return iris.data, iris.target


# ============================================================================
# PROBLEM 1: DECISION TREE WITH GINI INDEX
# ============================================================================
def problem_1_decision_tree_gini(X, y):
    """Build Decision Tree Classifier using GINI Index"""
    print("=" * 80)
    print("PROBLEM 1: Decision Tree Classifier (GINI Index)")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    dt_gini = DecisionTreeClassifier(
        criterion='gini',
        max_depth=4,
        min_samples_split=2,
        random_state=42
    )
    dt_gini.fit(X_train, y_train)

    # Predictions
    y_pred = dt_gini.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Parameters:")
    print(f"  - Criterion: GINI Index")
    print(f"  - Max Depth: 4")
    print(f"  - Min Samples Split: 2")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 2: DECISION TREE WITH ENTROPY
# ============================================================================
def problem_2_decision_tree_entropy(X, y):
    """Build Decision Tree Classifier using Entropy"""
    print("=" * 80)
    print("PROBLEM 2: Decision Tree Classifier (Entropy)")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    dt_entropy = DecisionTreeClassifier(
        criterion='entropy',
        max_depth=4,
        min_samples_split=2,
        random_state=42
    )
    dt_entropy.fit(X_train, y_train)

    # Predictions
    y_pred = dt_entropy.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Parameters:")
    print(f"  - Criterion: Entropy (Information Gain)")
    print(f"  - Max Depth: 4")
    print(f"  - Min Samples Split: 2")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 3: DECISION TREE WITH LOG LOSS
# ============================================================================
def problem_3_decision_tree_logloss(X, y):
    """Build Decision Tree Classifier using Log Loss"""
    print("=" * 80)
    print("PROBLEM 3: Decision Tree Classifier (Log Loss)")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    dt_logloss = DecisionTreeClassifier(
        criterion='log_loss',
        max_depth=4,
        min_samples_split=2,
        random_state=42
    )
    dt_logloss.fit(X_train, y_train)

    # Predictions
    y_pred = dt_logloss.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Parameters:")
    print(f"  - Criterion: Log Loss")
    print(f"  - Max Depth: 4")
    print(f"  - Min Samples Split: 2")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 4: LOGISTIC REGRESSION
# ============================================================================
def problem_4_logistic_regression(X, y):
    """Build Logistic Regression Classifier"""
    print("=" * 80)
    print("PROBLEM 4: Logistic Regression Classifier")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    log_reg = LogisticRegression(
        max_iter=200,
        random_state=42
    )
    log_reg.fit(X_train, y_train)

    # Predictions
    y_pred = log_reg.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel: Logistic Regression (Multi-class)")
    print(f"Accuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 5: BAGGING CLASSIFIER
# ============================================================================
def problem_5_bagging_classifier(X, y):
    """Build Bagging Classifier"""
    print("=" * 80)
    print("PROBLEM 5: Bagging Classifier")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    bagging_clf = BaggingClassifier(
        estimator=DecisionTreeClassifier(),
        n_estimators=100,
        random_state=42
    )
    bagging_clf.fit(X_train, y_train)

    # Predictions
    y_pred = bagging_clf.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel: Bagging Classifier")
    print(f"Base Estimator: Decision Tree")
    print(f"Number of Estimators: 100")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 6: RANDOM FOREST CLASSIFIER
# ============================================================================
def problem_6_random_forest(X, y):
    """Build Random Forest Classifier"""
    print("=" * 80)
    print("PROBLEM 6: Random Forest Classifier")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    rf_clf = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    rf_clf.fit(X_train, y_train)

    # Predictions
    y_pred = rf_clf.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel: Random Forest Classifier")
    print(f"Number of Trees: 100")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 7: GRADIENT BOOSTING CLASSIFIER
# ============================================================================
def problem_7_gradient_boosting(X, y):
    """Build Gradient Boosting Classifier"""
    print("=" * 80)
    print("PROBLEM 7: Gradient Boosting Classifier")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    gb_clf = GradientBoostingClassifier(
        n_estimators=100,
        random_state=42
    )
    gb_clf.fit(X_train, y_train)

    # Predictions
    y_pred = gb_clf.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel: Gradient Boosting Classifier")
    print(f"Number of Estimators: 100")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 8: ADABOOST CLASSIFIER
# ============================================================================
def problem_8_adaboost(X, y):
    """Build AdaBoost Classifier"""
    print("=" * 80)
    print("PROBLEM 8: AdaBoost Classifier")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # Build model
    ada_clf = AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=1),
        n_estimators=100,
        random_state=42
    )
    ada_clf.fit(X_train, y_train)

    # Predictions
    y_pred = ada_clf.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel: AdaBoost Classifier")
    print(f"Base Estimator: Decision Tree (max_depth=1)")
    print(f"Number of Estimators: 100")
    print(f"\nAccuracy Score: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\n" + "=" * 80 + "\n")

    return accuracy


# ============================================================================
# PROBLEM 9: PCA APPLICATION AND COMPARISON
# ============================================================================
def problem_9_pca_analysis(X, y):
    """Apply PCA and compare classifier performance"""
    print("=" * 80)
    print("PROBLEM 9: PCA Application and Comparison")
    print("=" * 80)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # --------------------------------------------------------------------
    # Part 1: Build classifier WITHOUT PCA
    # --------------------------------------------------------------------
    print("\n--- Part A: Classifier WITHOUT PCA ---")
    print("Using Random Forest Classifier")

    rf_without_pca = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_without_pca.fit(X_train, y_train)
    y_pred_without_pca = rf_without_pca.predict(X_test)
    accuracy_without_pca = accuracy_score(y_test, y_pred_without_pca)

    print(f"Number of Features: {X_train.shape[1]}")
    print(f"Accuracy WITHOUT PCA: {accuracy_without_pca:.4f} ({accuracy_without_pca * 100:.2f}%)")

    # --------------------------------------------------------------------
    # Part 2: Apply PCA for dimensionality reduction
    # --------------------------------------------------------------------
    print("\n--- Part B: Applying PCA ---")

    # Apply PCA with 2 components (for visualization and dimensionality reduction)
    pca = PCA(n_components=2, random_state=42)
    X_train_pca = pca.fit_transform(X_train)
    X_test_pca = pca.transform(X_test)

    print(f"Original number of features: {X_train.shape[1]}")
    print(f"Reduced number of features: {X_train_pca.shape[1]}")
    print(f"\nExplained Variance Ratio:")
    for i, var in enumerate(pca.explained_variance_ratio_, 1):
        print(f"  PC{i}: {var:.4f} ({var * 100:.2f}%)")
    print(f"Total Explained Variance: {sum(pca.explained_variance_ratio_):.4f} "
          f"({sum(pca.explained_variance_ratio_) * 100:.2f}%)")

    # --------------------------------------------------------------------
    # Part 3: Build classifier WITH PCA
    # --------------------------------------------------------------------
    print("\n--- Part C: Classifier WITH PCA ---")
    print("Using Random Forest Classifier")

    rf_with_pca = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_with_pca.fit(X_train_pca, y_train)
    y_pred_with_pca = rf_with_pca.predict(X_test_pca)
    accuracy_with_pca = accuracy_score(y_test, y_pred_with_pca)

    print(f"Number of Features: {X_train_pca.shape[1]}")
    print(f"Accuracy WITH PCA: {accuracy_with_pca:.4f} ({accuracy_with_pca * 100:.2f}%)")

    # --------------------------------------------------------------------
    # Part 4: Comparison
    # --------------------------------------------------------------------
    print("\n" + "-" * 80)
    print("COMPARISON RESULTS")
    print("-" * 80)
    print(f"Accuracy WITHOUT PCA: {accuracy_without_pca:.4f} ({accuracy_without_pca * 100:.2f}%)")
    print(f"Accuracy WITH PCA:    {accuracy_with_pca:.4f} ({accuracy_with_pca * 100:.2f}%)")
    print(f"Difference:           {abs(accuracy_without_pca - accuracy_with_pca):.4f}")

    if accuracy_with_pca >= accuracy_without_pca:
        print(f"\n✓ PCA maintained accuracy while reducing features from {X_train.shape[1]} to {X_train_pca.shape[1]}")
    else:
        print(f"\n⚠ PCA reduced features but with slight accuracy trade-off")

    print("\n" + "=" * 80 + "\n")

    return accuracy_without_pca, accuracy_with_pca


# ============================================================================
# MAIN EXECUTION
# ============================================================================
def main():
    """Execute all problem statements"""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "IRIS DATASET CLASSIFICATION SUITE" + " " * 25 + "║")
    print("║" + " " * 25 + "9 Problem Statements" + " " * 30 + "║")
    print("╚" + "=" * 78 + "╝")
    print("\n")

    # Load and explore data
    X, y = load_and_explore_data()

    # Store results
    results = {}

    # Execute all problems
    results['Problem 1 - DT (GINI)'] = problem_1_decision_tree_gini(X, y)
    results['Problem 2 - DT (Entropy)'] = problem_2_decision_tree_entropy(X, y)
    results['Problem 3 - DT (Log Loss)'] = problem_3_decision_tree_logloss(X, y)
    results['Problem 4 - Logistic Regression'] = problem_4_logistic_regression(X, y)
    results['Problem 5 - Bagging'] = problem_5_bagging_classifier(X, y)
    results['Problem 6 - Random Forest'] = problem_6_random_forest(X, y)
    results['Problem 7 - Gradient Boosting'] = problem_7_gradient_boosting(X, y)
    results['Problem 8 - AdaBoost'] = problem_8_adaboost(X, y)

    # Problem 9 returns two values
    acc_without_pca, acc_with_pca = problem_9_pca_analysis(X, y)
    results['Problem 9 - Without PCA'] = acc_without_pca
    results['Problem 9 - With PCA'] = acc_with_pca

    # Summary of all results
    print("=" * 80)
    print("SUMMARY OF ALL RESULTS")
    print("=" * 80)
    for problem, accuracy in results.items():
        print(f"{problem:<40}: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("=" * 80)

    # Find best model
    best_problem = max(results.items(), key=lambda x: x[1])
    print(f"\n🏆 Best Model: {best_problem[0]} with {best_problem[1]:.4f} accuracy")
    print("\n")


if __name__ == "__main__":
    main()