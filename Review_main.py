__author__ = 'Simons'
import nltk
import csv
from Functions import*
import tfidf

rest = open('madison_restaurant_info')
user = open('madison_user_list.csv')
review = open('reviews.csv')
resta = csv.reader(rest)
reviews = csv.reader(review)
users = csv.reader(user)
reviews1 = findStoreReviews(resta)
reviews2 = findUserReviews(users)
reviews3 = preProcessReviews(reviews1)
reviews4 = preProcessReviews(reviews2)
result = compare(reviews1, reviews2)
f=open("Madison.csv",'w',encoding='utf8',newline='')
writer = csv.writer(f)
writer.writerows(result)