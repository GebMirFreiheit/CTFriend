import sys
import numpy as np
import pickle
import re
import pymorphy2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# очистка текста с помощью regexp приведение слов в инфинитив и нижний регистр, замена цифр


def text_cleaner(text):
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    text = text.lower()  # приведение в lowercase
    text = text.strip()
    text = ' '.join(morph.parse(
        word)[0].normal_form for word in text.split() if len(word) > 2)
    return text


# загрузка данных из файла model.txt

def load_data():
    data = {'text': [], 'tag': []}
    for line in open('dataset1.txt'):
        row = line.split("@")
        data['text'].append(row[0])
        data['tag'].append(row[1].strip())
    return data

# Обучение


def train_test_split(data, validation_split=0.1):
    sz = len(data['text'])
    indices = np.arange(sz)
    np.random.shuffle(indices)

    X = [data['text'][i] for i in indices]
    Y = [data['tag'][i] for i in indices]
    nb_validation_samples = int(validation_split * sz)

    return {
        'train': {'x': X[:-nb_validation_samples], 'y': Y[:-nb_validation_samples]},
        'test': {'x': X[-nb_validation_samples:], 'y': Y[-nb_validation_samples:]}
    }


# - - - -

def openai():
    data = load_data()
    D = train_test_split(data)
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SGDClassifier(loss='log_loss')),
    ])
    text_clf.fit(D['train']['x'], D['train']['y'])
    # predicted = text_clf.predict(D['train']['x'])
    return text_clf
