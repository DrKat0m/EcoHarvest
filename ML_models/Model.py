import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
import numpy as np
import pickle

# Load the dataset
df = pd.read_csv('Files/Crop_recommendation.csv')

# Examine the distribution of the labels
print(df['label'].value_counts())

# Splitting data and labels
X = df[['temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Balance the dataset
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Split the resampled data
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# SVM Model
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("SVM Results:")
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Feature importance for SVM
print("Feature Importance for SVM:")
print(pd.DataFrame(clf.coef_, columns=X.columns))

# Random Forest Model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Random Forest Results:")
print(accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Hyperparameter tuning for SVM using GridSearchCV
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': [1, 0.1, 0.01, 0.001],
    'kernel': ['linear', 'rbf']
}

grid_search = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)
grid_search.fit(X_train, y_train)

best_svc = grid_search.best_estimator_
y_pred_grid = best_svc.predict(X_test)


print('prediction ------------------------')
answer = (clf.predict(np.array([10.891666666666666, 80, 7.026999999999882, 107.95]).reshape(1, -1)))
probs = clf.predict_proba(np.array([10.891666666666666, 80, 7.026999999999882, 107.95]).reshape(1, -1))
best_n = np.argsort(probs, axis=1)[:,-5:]
print("-------------")
print(answer)
answer = clf.classes_[best_n][0]
answer = list(answer)
answer.reverse()
print(answer)

print("Best SVM with Grid Search Results:")
print(accuracy_score(y_test, y_pred_grid))
print(classification_report(y_test, y_pred_grid))
