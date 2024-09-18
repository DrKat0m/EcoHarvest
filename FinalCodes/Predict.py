import pickle
import numpy as np

def predict_crop(temeperature, humidity, ph, rainfall):
    filename = "finalized_model.sav"
    clf = pickle.load(open(filename, 'rb'))
    # Real life predictions
    answer = (clf.predict(np.array([temeperature, humidity, ph, rainfall]).reshape(1, -1)))
    probs = clf.predict_proba(np.array([temeperature, humidity, ph, rainfall]).reshape(1, -1))
    best_n = np.argsort(probs, axis=1)[:,-4:]
    print("-------------")
    print(answer)
    answer = clf.classes_[best_n][0]
    answer = list(answer)
    answer.reverse()
    return answer

