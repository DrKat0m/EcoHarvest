import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the data
data = pd.read_csv("Files/Crop_recommendation.csv")

# Shuffle the dataset
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# Display class distribution
print(data['label'].value_counts())

# Split the data into training and testing sets
X = data[['temperature', 'humidity', 'ph', 'rainfall']]
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train a Random Forest model with OOB score
clf = RandomForestClassifier(n_estimators=50, oob_score=True, random_state=42)
clf.fit(X_train, y_train)
print(f"OOB Score: {clf.oob_score_:.2f}")
filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))

# Cross-validation with Stratified KFolds
strat_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(clf, X, y, cv=strat_kfold, scoring='accuracy')
print(f"Cross-validation scores: {cv_scores}")
print(f"Average CV Score: {cv_scores.mean():.2f}")

# Predictions on the test set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy*100:.2f}%")


# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Feature importances
feature_importances = clf.feature_importances_
for feature, importance in zip(X.columns, feature_importances):
    print(f"{feature}: {importance:.4f}")

