from Yelp_save import Yelp_reload_list,Yelp_reload_dict,Yelp_save_list
from Yelp_recommender import Yelp_recommender
import numpy
import csv


if __name__ == "__main__":
	
	madison_user_list_path = "madison_user_list.pkl"
	madison_user_list = Yelp_reload_list(madison_user_list_path)
	madison_restaurant_list_path = "madison_restaurant_list.pkl"
	madison_restaurant_list = Yelp_reload_list(madison_restaurant_list_path)
	madison_user_rating_path = "madison_user_rating_dict.json"	
	madison_user_rating_dict = Yelp_reload_dict(madison_user_rating_path)
	madison_user_mean = Yelp_recommender.get_mean_from_user(madison_user_rating_dict,madison_user_list)
	madison_user_rating_matrix = Yelp_recommender.get_rating_matrix(madison_user_rating_dict,madison_user_list,madison_restaurant_list)
	madison_item_similarity_matrix = Yelp_recommender.get_item_similarity_matrix(madison_user_rating_matrix,madison_user_mean,method="Euclidean")
	madison_score_matrix = Yelp_recommender.calculate_item_scores(madison_item_similarity_matrix,madison_user_rating_matrix)
	madison_user_similarity_matrix = Yelp_recommender.calculate_user_similarity(madison_user_rating_dict,madison_user_list,madison_restaurant_list,madison_score_matrix,madison_user_mean)
	madison_estimating_score_matrix = Yelp_recommender.KNN(madison_user_similarity_matrix,madison_score_matrix,madison_user_mean,k=10)
	madison_recommend = Yelp_recommender.recommend(madison_estimating_score_matrix)
	recommend_file = open("madison_recommend.csv","wb")
	wr = csv.writer(recommend_file,dialect = "excel")
	wr.writerows(madison_recommend)
	

	edinburgh_user_list_path = "edinburgh_user_list.pkl"
	edinburgh_user_list = Yelp_reload_list(edinburgh_user_list_path)
	edinburgh_restaurant_list_path = "edinburgh_restaurant_list.pkl"
	edinburgh_restaurant_list = Yelp_reload_list(edinburgh_restaurant_list_path)
	edinburgh_user_rating_path = "edinburgh_user_rating_dict.json"	
	edinburgh_user_rating_dict = Yelp_reload_dict(edinburgh_user_rating_path)
	edinburgh_user_mean = Yelp_recommender.get_mean_from_user(edinburgh_user_rating_dict,edinburgh_user_list)
	edinburgh_user_rating_matrix = Yelp_recommender.get_rating_matrix(edinburgh_user_rating_dict,edinburgh_user_list,edinburgh_restaurant_list)
	edinburgh_item_similarity_matrix = Yelp_recommender.get_item_similarity_matrix(edinburgh_user_rating_matrix,edinburgh_user_mean,method="Pearson")
	edinburgh_score_matrix = Yelp_recommender.calculate_item_scores(edinburgh_item_similarity_matrix,edinburgh_user_rating_matrix)
	
	error = Yelp_recommender.evaluate_recommendation(score_matrix,user_rating_dict,user_list,restaurant_list)
	
	
	edinburgh_user_similarity_matrix = Yelp_recommender.calculate_user_similarity(edinburgh_user_rating_dict,edinburgh_user_list,edinburgh_restaurant_list,edinburgh_score_matrix,edinburgh_user_mean)
	edinburgh_estimating_score_matrix = Yelp_recommender.KNN(edinburgh_user_similarity_matrix,edinburgh_score_matrix,edinburgh_user_mean,k=10)
	edinburgh_recommend = Yelp_recommender.recommend(edinburgh_estimating_score_matrix)
	recommend_file = open("edinburgh_recommend.csv","wb")
	wr = csv.writer(recommend_file,dialect = "excel")
	wr.writerows(edinburgh_recommend)
	"""
	error = Yelp_recommender.evaluate_recommendation(estimating_rating_matrix,user_rating_dict,user_list,restaurant_list)
	error_list.append(error)
	print error_list
	"""
	
	pittsburgh_user_list_path = "pittsburgh_user_list.pkl"
	pittsburgh_user_list = Yelp_reload_list(pittsburgh_user_list_path)
	pittsburgh_restaurant_list_path = "pittsburgh_restaurant_list.pkl"
	pittsburgh_restaurant_list = Yelp_reload_list(pittsburgh_restaurant_list_path)
	pittsburgh_user_rating_path = "pittsburgh_user_rating_dict.json"	
	pittsburgh_user_rating_dict = Yelp_reload_dict(pittsburgh_user_rating_path)
	pittsburgh_user_mean = Yelp_recommender.get_mean_from_user(pittsburgh_user_rating_dict,pittsburgh_user_list)
	pittsburgh_user_rating_matrix = Yelp_recommender.get_rating_matrix(pittsburgh_user_rating_dict,pittsburgh_user_list,pittsburgh_restaurant_list)
	pittsburgh_item_similarity_matrix = Yelp_recommender.get_item_similarity_matrix(pittsburgh_user_rating_matrix,pittsburgh_user_mean,method="Euclidean")
	pittsburgh_score_matrix = Yelp_recommender.calculate_item_scores(pittsburgh_item_similarity_matrix,pittsburgh_user_rating_matrix)
	pittsburgh_user_similarity_matrix = Yelp_recommender.calculate_user_similarity(pittsburgh_user_rating_dict,pittsburgh_user_list,pittsburgh_restaurant_list,pittsburgh_score_matrix,edinburgh_user_mean)
	pittsburgh_estimating_score_matrix = Yelp_recommender.KNN(pittsburgh_user_similarity_matrix,pittsburgh_score_matrix,pittsburgh_user_mean,k=10)
	pittsburgh_recommend = Yelp_recommender.recommend(pittsburgh_estimating_score_matrix)
	recommend_file = open("pittsburgh_recommend.csv","wb")
	wr = csv.writer(recommend_file,dialect = "excel")
	wr.writerows(pittsburgh_recommend)
	





