from __future__ import with_statement
from __future__ import division
import json
import csv
import sys
import math
import numpy
import pandas
import pickle
from Yelp_get import Yelp_get
from Yelp_data import Yelp_data
from Yelp_save import Yelp_reload_list,Yelp_reload_dict,Yelp_save_list,Yelp_save_dict
from math import sqrt

class Yelp_recommender(object):
	"""
	docstring for Recommendation_Yelp
	
	"""

	@staticmethod
	def get_user_rating(review):
		review_id_list = review.keys()
		review_all_user = [review[review_id]["user_id"] for review_id in review_id_list]
		user_list = list(set(review_all_user))
		rating = {}
		for user_id in user_list:
			all_review = {}
			indices = [index for index, user in enumerate(review_all_user) if user == user_id]
			for num in range(len(indices)):
				business_id = review[review_id_list[indices[num]]]["business_id"]
				all_review[business_id] = review[review_id_list[indices[num]]]["stars"]
			rating[user_id] = all_review
		return rating

	@staticmethod
	def get_item_rating(review):
		review_id_list = review.keys()
		review_all_business = [review[review_id]["business_id"] for review_id in review_id_list]
		business_list = list(set(review_all_business))
		rating = {}
		for business_id in business_list:
			all_review = {}
			indices = [index for index, business in enumerate(review_all_business) if business == business_id]
			for num in range(len(indices)):
				user_id = review[review_id_list[indices[num]]]["user_id"]
				all_review[user_id] = review[review_id_list[indices[num]]]["stars"]
			rating[business_id] = all_review
		return rating

	@staticmethod
	def get_rating_matrix(rating_dict,user_list,item_list):
		rating_matrix = []
		for user in user_list:
			rating_vector = [0]*len(item_list)
			indices = [item_list.index(item) for item in rating_dict[user].keys()]
			rating_vector = numpy.array(rating_vector)
			rating_vector[indices] = rating_dict[user].values()
			rating_matrix.append(list(rating_vector))
		return numpy.array(rating_matrix)

	@staticmethod
	def get_user_rating_matrix(rating_dict,user_list,item_list):
		rating_matrix = numpy.empty((1,len(item_list)),dtype=float)
		file = open("user_rating_matrix.csv","wb")
		wr = csv.writer(file,dialect="excel")
		wr.writerows(item_list)
		for user in user_list:
			rating_vector = numpy.zeros((1,len(item_list)))
			indices = [item_list.index(item) for item in rating_dict[user].keys()]
			rating_vector[0,indices] = rating_dict[user].values()
			wr.writerows(rating_vector)


	@staticmethod
	def get_mean_from_user(user_rating_dict,user_list):
		mean_list = [sum(user_rating_dict[user_id].values())/len(user_rating_dict[user_id].keys()) for user_id in user_list]
		return mean_list


	@staticmethod
	def get_item_similarity_matrix(user_rating_matrix,user_mean,method="Pearson"):
		item_rating_matrix = numpy.transpose(user_rating_matrix)
		item_num = numpy.shape(item_rating_matrix)[0]
		similarity_matrix = []
		user_num = numpy.shape(item_rating_matrix)[1]
		for row in range(item_num):
			similarity_vector = [0]*item_num
			for col in range(row,item_num):
				item_rating_vector1 = item_rating_matrix[row,]-numpy.array(user_mean) 
				item_rating_vector2 = item_rating_matrix[col,]-numpy.array(user_mean)
				similarity = Yelp_recommender.calculate_similarity(item_rating_vector1,item_rating_vector2,method=method)
				similarity_vector[col] = similarity
			similarity_matrix.append(similarity_vector)
		similarity_matrix = numpy.array(similarity_matrix)
		for col in range(item_num):
			for row in range(col,item_num):
				similarity_matrix[row,col] = similarity_matrix[col,row]
		return similarity_matrix
	
	@staticmethod
	def calculate_item_scores(similarity_matrix,user_rating_matrix):
		user_num = numpy.shape(user_rating_matrix)[0]
		item_num = numpy.shape(user_rating_matrix)[1]
		score_matrix = numpy.full((user_num,item_num),0,dtype=float)
		for user in range(user_num):
			for item in range(item_num):
				score = numpy.sum(similarity_matrix[item,]*user_rating_matrix[user,])/numpy.sum(similarity_matrix[item,])
				score_matrix[user,item] = score
		return score_matrix

	@staticmethod
	def calculate_user_similarity(user_rating_dict,user_list,restaurant_list,score_matrix,user_mean):
		similarity_matrix = []
		for row in range(len(user_list)):
			similarity_vector = []
			list1 = user_rating_dict[user_list[row]].keys()
			mean1 = user_mean[row]
			for col in range(row,len(user_list)):		
				list2 = user_rating_dict[user_list[col]].keys()
				mean2 = user_mean[col]
				join_list = list(set(list1+list2))
				rating_vector1 = []
				rating_vector2 = []
				for item in join_list:
					if item in list1:
						rating_vector1.append(user_rating_dict[user_list[row]][item]-mean1)
					else:
						rating_vector1.append(score_matrix[row,restaurant_list.index(item)]-mean1)
					if item in list2:
						rating_vector2.append(user_rating_dict[user_list[col]][item]-mean2)
					else:
						rating_vector2.append(score_matrix[col,restaurant_list.index(item)]-mean2)
				similarity = numpy.sum(numpy.array(rating_vector1)*numpy.array(rating_vector2))/sqrt(numpy.sum(numpy.square(rating_vector1))*numpy.sum(numpy.square(rating_vector2)))
				similarity_vector.append(similarity)
			similarity_matrix.append(similarity_vector)
		similarity_matrix = numpy.array(similarity_matrix)
		for col in range(len(user_list)):
			for row in range(col,len(user_list)):
				similarity_matrix[row,col] = similarity_matrix[col,row]
		return similarity_matrix

	@staticmethod
	def KNN(user_similarity_matrix,score_matrix,user_mean,k=10):
		user_num = numpy.shape(score_matrix)[0]
		item_num = numpy.shape(score_matrix)[1]
		esitmating_rating_matrix = []
		for row in range(user_num):
			rating_vector = []
			for col in range(item_num):
				neighborhood_rating = score_matrix[numpy.argsort(user_similarity_matrix[row,])[0:k],col]-numpy.array(user_mean)[0,numpy.argsort(user_similarity_matrix[row,])[0:k]]
				rating = user_mean[row]+1/numpy.sum(numpy.sort(user_similarity_matrix[row,])[0:k])*numpy.sum(numpy.sort(user_similarity_matrix[row,])[0:k]*neighborhood_rating)
				rating_vector.append(rating)
			esitmating_rating_matrix.append(rating_vector)
		return numpy.array(esitmating_rating_matrix)

	@staticmethod
	def evaluate_recommendation(estimating_rating_matrix,user_rating_dict,user_list,restaurant_list):
		error = []
		for row in range(len(user_list)):
			for col in range(len(restaurant_list)):
				if restaurant_list[col] in user_rating_dict[user_list[row]].keys():
					errors = float(user_rating_dict[user_list[row]][restaurant_list[col]])-estimating_rating_matrix[row,col]
					error.append(errors)
		error = numpy.array(error)
		MSE = numpy.sum(numpy.square(error))/numpy.size(error)
		return MSE

	@staticmethod
	def recommend(estimating_rating_matrix):
		user_num = numpy.shape(estimating_rating_matrix)[0]
		recommend_matrix = []
		for num in range(user_num):
			indices = numpy.argsort(estimating_rating_matrix[num,])[0:200]
			recommend_matrix.append(indices.tolist())
			#numpy.array(recommend_matrix,dtype=int)
		return recommend_matrix

	@staticmethod
	def combine_score(estimating_rating_matrix,nltk_rating_matrix):
		combined_score = 0.5*estimating_rating_matrix+0.5*nltk_rating_matrix
		return combined_score

	@staticmethod
	def calculate_similarity(vector1,vector2,method="Pearson"):
		if method == "Pearson":
			nominator = numpy.sum(vector1*vector2)
			denominator = sqrt(numpy.sum(numpy.square(vector1))*numpy.sum(numpy.square(vector2)))
			similarity = nominator/denominator
		elif method == "Euclidean":
			distance = sqrt(numpy.sum(numpy.square(vector1 - vector2)))
			similarity = 1/(1+distance)
		elif method == "Spearman":
			distance = vector2 - vector1
			n = len(vector2)
			similarity = 1-6*numpy.sum(numpy.square(distance))/(n*(n**2-1))
		return similarity
	
	@staticmethod
	def revise_user_weights(user,user_list):
		weight = []
		for user_id in user_list:
			info = user[user_id]
			weights = (int(info["votes_funny"])+int(info["votes_cool"])+int(info["votes_useful"]))*0.001+(2015-int(info["yelping_since"][0:4]))*0.1+int(info["review_count"])*0.01+len(info["friends"])*0.1
			weight.append(weights)
		return weight
	
	@staticmethod
	def revise_rating(restaurant_rating_dict,weight_list,user_list,restaurant_list):
		stars_new_list = []
		for restaurant_id in restaurant_list:
			stars_new = 0
			factor = 0
			for user_id in restaurant_rating_dict[restaurant_id].keys():
				if user_id in user_list:
					index = user_list.index(user_id)
					stars_new += restaurant_rating_dict[restaurant_id][user_id]*weight_list[index]
					factor += weight_list[index]
			stars_new = stars_new/factor
			stars_new_list.append(stars_new)
		return stars_new_list
	@staticmethod
	def get_new_recommend_restaurant(new_rating_list,restaurant_list):
		new_rating_list = numpy.array(new_rating_list)
		index = numpy.argsort(new_rating_list)
		restaurant_index = index.tolist()
		new_list = [restaurant_list[num] for num in restaurant_index] 
		return new_list


	def __init__(self, user, review, business):
		super(Recommendation_Yelp, self).__init__()
		self.user = user
		self.review = review
		self.business = business


if __name__ == "__main__":
	"""
	user_mean = Yelp_recommender.get_mean_from_user(user_rating_dict,user_list)
	user_path = "user.json"				
	review_restaurant_path = "review_restaurant.json"
	restaurant_path = "restaurant.json"
	user = Yelp_reload_user(user_path)
	"""
	review_restaurant_path = "review_restaurant.json"
	review_restaurant = Yelp_reload_dict(review_restaurant_path)	
	#user_rating_dict = Yelp_recommender.get_user_rating(review_restaurant)
	
	restaurant_path = "restaurant.json"
	restaurant = Yelp_reload_dict(restaurant_path)
	las_vegas_restaurant = {}
	for restaurant_id in restaurant.keys():
		if restaurant[restaurant_id]["city"]=="Las Vegas":
			las_vegas_restaurant[restaurant_id] = restaurant[restaurant_id]
	las_vegas_business_list = las_vegas_restaurant.keys()
	las_vegas_review = {}
	las_vegas_restaurant_list = []
	las_vegas_user_list = []
	for review_id in review_restaurant.keys():
		if review_restaurant[review_id]["business_id"] in las_vegas_business_list:
			#las_vegas_review[review_id] = review_restaurant[review_id]
			las_vegas_restaurant_list.append(review_restaurant[review_id]["business_id"])
			las_vegas_user_list.append(review_restaurant[review_id]["user_id"])
	"""
	with open("las_vegas_review.json","wb") as file:
		json.dump(las_vegas_review,file)
	file.close()
	"""
	with open("las_vegas_user_list.pkl","wb") as file:
		pickle.dump(las_vegas_user_list,file)
	file.close()
	with open("las_vegas_restaurant_list.pkl","wb") as file:
		pickle.dump(las_vegas_restaurant_list,file)
	file.close()
	
	






		