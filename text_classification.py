from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.datasets as skd
import os
import shutil
import time


def classified_topic(name_file):
    categories = ['ව්යාපාරික', 'විනෝදාස්වාදය', 'දේශීය', 'ක්රීඩා', 'ලෝකය']
    sinhala_train = skd.load_files(
        'Dataset\Train', categories=categories, encoding='utf-8')
    sinhala_test = skd.load_files(
        'Dataset\Test', categories=categories, encoding='utf-8')

    #file = name_file

    B = open(os.path.join('uploads', name_file), encoding='utf-8')

    sinhala_test_1 = B.read()

    ENCODING = 'utf-8'
    vectorizer = TfidfVectorizer(encoding=ENCODING, use_idf=True, norm='l2', binary=False, sublinear_tf=True,
                                 min_df=0.001, max_df=1.0, ngram_range=(1, 2), analyzer='word', stop_words=None)

    # the output of the fit_transform (x_train) is a sparse csc matrix.
    X_train = vectorizer.fit_transform(sinhala_train.data)

    clf = LinearSVC(loss='squared_hinge', penalty='l2',
                    dual=False, tol=1e-3, class_weight='balanced')
    clf.fit(X_train, sinhala_train.target)

    X_test = vectorizer.transform(sinhala_test.data)
    pred = clf.predict(X_test)

    from sklearn import metrics
    from sklearn.metrics import accuracy_score
    print("Accuracy of the model:", accuracy_score(
        sinhala_test.target, pred))
    print(metrics.classification_report(sinhala_test.target,
          pred, target_names=sinhala_test.target_names)),
    metrics.confusion_matrix(sinhala_test.target, pred)

    docs_new1 = sinhala_test_1
    docs_new = [docs_new1]

    X_new_tfidf = vectorizer.transform(docs_new)

    predicted_topic = clf.predict(X_new_tfidf)

    for doc, category in zip(docs_new, predicted_topic):
        topic = (sinhala_train.target_names[category])

    dstDir = os.path.join('New data', topic)
    move_file = os.path.join('uploads', name_file)
    B.close()
    shutil.move(move_file, dstDir)
    return topic
