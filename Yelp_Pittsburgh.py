from Yelp_save import Yelp_reload_list,Yelp_reload_dict,Yelp_save_list,Yelp_save_dict,Yelp_save_csv
from Yelp_recommender import Yelp_recommender
from Yelp_data import Yelp_data

if __name__ == "__main__":
	restaurant_path = "restaurant.json"
	restaurant = Yelp_reload_dict(restaurant_path)
	review_restaurant_path = "review_restaurant.json"
	review_restaurant = Yelp_reload_dict(review_restaurant_path)
	pittsburgh_restaurant = {}
	for restaurant_id in restaurant.keys():
		if str(restaurant[restaurant_id]["city"])=="Pittsburgh":
			pittsburgh_restaurant[restaurant_id] = restaurant[restaurant_id]
	pittsburgh_business_list = pittsburgh_restaurant.keys()
	pittsburgh_review = {}
	pittsburgh_restaurant_list = []
	pittsburgh_user_list = []
	for review_id in review_restaurant.keys():
		if review_restaurant[review_id]["business_id"] in pittsburgh_business_list:
			pittsburgh_review[review_id] = review_restaurant[review_id]
			pittsburgh_restaurant_list.append(review_restaurant[review_id]["business_id"])
			pittsburgh_user_list.append(review_restaurant[review_id]["user_id"])
	pittsburgh_restaurant_list = list(set(pittsburgh_restaurant_list))
	pittsburgh_user_list = list(set(pittsburgh_user_list))
	pittsburgh_user_info = []
	user_path = "user.json"
	user = Yelp_reload_dict(user_path)
	for user_id in pittsburgh_user_list:
		user_info = Yelp_data.get_user_info(user,user_id)
		pittsburgh_user_info.append([user_id,user_info["name"]])

	pittsburgh_user_rating_dict = Yelp_recommender.get_user_rating(pittsburgh_review)
	pittsburgh_item_rating_dict = Yelp_recommender.get_item_rating(pittsburgh_review)
	pittsburgh_restaurant_info = []
	for restaurant_id in pittsburgh_restaurant_list:
		restaurant_info = Yelp_data.get_restaurant_info(pittsburgh_restaurant,restaurant_id)
		pittsburgh_restaurant_info.append([restaurant_id,restaurant_info["full_address"],restaurant_info["name"]])
	pittsburgh_new_weight_list = Yelp_recommender.revise_user_weights(user,pittsburgh_user_list)
	pittsburgh_new_rating_list = Yelp_recommender.revise_rating(pittsburgh_item_rating_dict,pittsburgh_new_weight_list,pittsburgh_user_list,pittsburgh_restaurant_list)
	pittsburgh_new_restaurant_info = Yelp_recommender.get_new_recommend_restaurant(pittsburgh_new_rating_list,pittsburgh_restaurant_info)
	Yelp_save_csv("pittsburgh_new_restaurant_info.csv",pittsburgh_new_restaurant_info)
	Yelp_save_csv("pittsburgh_user_info.csv",pittsburgh_user_info)
	Yelp_save_csv("pittsburgh_restaurant_info.csv",pittsburgh_restaurant_info)
	Yelp_save_list("pittsburgh_restaurant_info.pkl",pittsburgh_restaurant_info)
	Yelp_save_list("pittsburgh_restaurant_list.pkl",pittsburgh_restaurant_list)
	Yelp_save_list("pittsburgh_user_list.pkl",pittsburgh_user_list)
	Yelp_save_list("pittsburgh_user_info.pkl",pittsburgh_user_info)
	Yelp_save_dict("pittsburgh_review.json",pittsburgh_review)
	Yelp_save_dict("pittsburgh_user_rating_dict.json",pittsburgh_user_rating_dict)
	Yelp_save_dict("pittsburgh_item_rating_dict.json",pittsburgh_item_rating_dict)
	Yelp_save_list("pittsburgh_new_rating_list.pkl",pittsburgh_new_rating_list)
	




