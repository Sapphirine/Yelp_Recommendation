__author__ = 'Simons'
from main import*
from nltk.corpus import stopwords
from collections import Counter
from nltk import*
import types
import tfidf

def preProcessReviews(list):
    porter = nltk.PorterStemmer()
    stop = stopwords.words("english")
    temp = []
    i = 0;
    G = []
    for row in list:
        token = nltk.word_tokenize(row[8])
        '''print(token)'''
        temp = ' '.join([a for a in token if a not in stop])
        '''print(temp)'''
        temp = nltk.word_tokenize(temp)
        stem = [porter.stem(t) for t in temp]
        '''print(stem)'''
        row[8] = stem
        row.append(stem)
    for row in list:
        print(row[9])
    return list

    '''words = ' '.join([a for a in reviews[i].split() if a not in stop])'''

def findStoreId(store_name):
    store_id = 'null'
    for row in store:
        if(store_name == row[6]):
            store_id = row[1]
    if (store_id == 'null'):
        print('Restaurant not found!')
    else:
        return store_id

def findStoreName(store_id):
    store_name = 'null'
    for row in store:
        if(store_id == row[1]):
            store_name = row[6]
    if (store_name == 'null'):
        print('Restaurant not found!')
    else:
        return store_name

def findUserReviews(user_id):
    user_reviews=[]
    for row in reviews:
        if user_id == row[1]:
            user_reviews.append(row[8])
    return user_reviews

def findStoreReviews(store_id):
    store_revies=[]
    for row in reviews:
        if store_id == row[2]:
            store_reviews.append(row[8])
    return store_reviews


def normalize(list):
    length = len(list)
    t = 0
    for i in range(length):
        if t < list[i]:
            t = list[i]
    for i in range(length):
        list[i]=list[i]/t
    return list


def compare (list1,list2,list3):
    g = []
    for rows in list1:
        for rows in list2:
             g.extend(tfidf(list1.rows[8],list2.rows[8],list3[rownumber]))
    g = sorted(g,key=getKey)
    g = normalize(g)
    return g




