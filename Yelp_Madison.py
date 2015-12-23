from Yelp_save import Yelp_reload_list,Yelp_reload_dict,Yelp_save_list,Yelp_save_dict,Yelp_save_csv
from Yelp_recommender import Yelp_recommender
from Yelp_data import Yelp_data

if __name__ == "__main__":
	restaurant_path = "restaurant.json"
	restaurant = Yelp_reload_dict(restaurant_path)
	review_restaurant_path = "review_restaurant.json"
	review_restaurant = Yelp_reload_dict(review_restaurant_path)
	madison_restaurant = {}
	for restaurant_id in restaurant.keys():
		if restaurant[restaurant_id]["city"]=="Madison":
			madison_restaurant[restaurant_id] = restaurant[restaurant_id]
	madison_business_list = madison_restaurant.keys()
	madison_review = {}
	madison_restaurant_list = []
	madison_user_list = []
	for review_id in review_restaurant.keys():
		if review_restaurant[review_id]["business_id"] in madison_business_list:
			madison_review[review_id] = review_restaurant[review_id]
			madison_restaurant_list.append(review_restaurant[review_id]["business_id"])
			madison_user_list.append(review_restaurant[review_id]["user_id"])
	madison_restaurant_list = list(set(madison_restaurant_list))
	madison_user_list = list(set(madison_user_list))
	madison_user_info = []
	user_path = "user.json"
	user = Yelp_reload_dict(user_path)
	for user_id in madison_user_list:
		user_info = Yelp_data.get_user_info(user,user_id)
		madison_user_info.append([user_id,user_info["name"]])

	madison_user_rating_dict = Yelp_recommender.get_user_rating(madison_review)
	madison_item_rating_dict = Yelp_recommender.get_item_rating(madison_review)
	madison_restaurant_info = []
	for restaurant_id in madison_restaurant_list:
		restaurant_info = Yelp_data.get_restaurant_info(madison_restaurant,restaurant_id)
		madison_restaurant_info.append([restaurant_id,restaurant_info["full_address"],restaurant_info["name"]])
	new_weight_list = Yelp_recommender.revise_user_weights(user,madison_user_list)
	new_rating_list = Yelp_recommender.revise_rating(madison_item_rating_dict,new_weight_list,madison_user_list,madison_restaurant_list)
	madison_new_restaurant_info = Yelp_recommender.get_new_recommend_restaurant(madison_new_rating_list,madison_restaurant_info)
	Yelp_save_csv("madison_new_restaurant_info.csv",madison_new_restaurant_info)
	Yelp_save_csv("madison_user_info.csv",madison_user_info)
	Yelp_save_csv("madison_restaurant_info.csv",madison_restaurant_info)
	Yelp_save_list("madison_restaurant_info.pkl",madison_restaurant_info)
	Yelp_save_list("madison_restaurant_list.pkl",madison_restaurant_list)
	Yelp_save_list("madison_user_list.pkl",madison_user_list)
	Yelp_save_list("madison_user_info.pkl",madison_user_info)
	Yelp_save_dict("madison_review.json",madison_review)
	Yelp_save_dict("madison_user_rating_dict.json",madison_user_rating_dict)
	Yelp_save_dict("madison_item_rating_dict.json",madison_item_rating_dict)
	Yelp_save_list("madison_new_rating_list.pkl",new_rating_list)
	