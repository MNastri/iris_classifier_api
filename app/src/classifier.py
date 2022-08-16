from os import getcwd
from os.path import join

import joblib

from sklearn.svm import SVC

classifier_filename = "iris_classifier.joblib"
basepath_of_classifier = getcwd()
classifier_fullpath = join(basepath_of_classifier, classifier_filename)
classifier: SVC = joblib.load(filename=classifier_fullpath)
