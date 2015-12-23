from Yelp_save import Yelp_reload_list,Yelp_reload_dict,Yelp_save_list,Yelp_save_dict,Yelp_save_csv
from Yelp_recommender import Yelp_recommender
from Yelp_data import Yelp_data

if __name__ == "__main__":
	restaurant_path = "restaurant.json"
	restaurant = Yelp_reload_dict(restaurant_path)
	review_restaurant_path = "review_restaurant.json"
	review_restaurant = Yelp_reload_dict(review_restaurant_path)
	edinburgh_restaurant = {}
	for restaurant_id in restaurant.keys():
		if str(restaurant[restaurant_id]["city"])=="Edinburgh":
			edinburgh_restaurant[restaurant_id] = restaurant[restaurant_id]
	edinburgh_business_list = edinburgh_restaurant.keys()
	edinburgh_review = {}
	edinburgh_restaurant_list = []
	edinburgh_user_list = []
	for review_id in review_restaurant.keys():
		if review_restaurant[review_id]["business_id"] in edinburgh_business_list:
			edinburgh_review[review_id] = review_restaurant[review_id]
			edinburgh_restaurant_list.append(review_restaurant[review_id]["business_id"])
			edinburgh_user_list.append(review_restaurant[review_id]["user_id"])
	edinburgh_restaurant_list = list(set(edinburgh_restaurant_list))
	edinburgh_user_list = list(set(edinburgh_user_list))
	edinburgh_user_info = []
	user_path = "user.json"
	user = Yelp_reload_dict(user_path)
	for user_id in edinburgh_user_list:
		user_info = Yelp_data.get_user_info(user,user_id)
		edinburgh_user_info.append([user_id,user_info["name"]])

	edinburgh_user_rating_dict = Yelp_recommender.get_user_rating(edinburgh_review)
	edinburgh_item_rating_dict = Yelp_recommender.get_item_rating(edinburgh_review)
	edinburgh_restaurant_info = []
	for restaurant_id in edinburgh_restaurant_list:
		restaurant_info = Yelp_data.get_restaurant_info(edinburgh_restaurant,restaurant_id)
		edinburgh_restaurant_info.append([restaurant_id,restaurant_info["full_address"],restaurant_info["name"]])
	new_weight_list = Yelp_recommender.revise_user_weights(user,edinburgh_user_list)
	new_rating_list = Yelp_recommender.revise_rating(edinburgh_item_rating_dict,new_weight_list,edinburgh_user_list,edinburgh_restaurant_list)
	edinburgh_new_restaurant_info = Yelp_recommender.get_new_recommend_restaurant(edinburgh_new_rating_list,edinburgh_restaurant_info)
	Yelp_save_csv("edinburgh_new_restaurant_info.csv",edinburgh_new_restaurant_info)
	Yelp_save_csv("edinburgh_user_info.csv",edinburgh_user_info)
	Yelp_save_csv("edinburgh_restaurant_info.csv",edinburgh_restaurant_info)
	Yelp_save_list("edinburgh_restaurant_info.pkl",edinburgh_restaurant_info)
	Yelp_save_list("edinburgh_restaurant_list.pkl",edinburgh_restaurant_list)
	Yelp_save_list("edinburgh_user_list.pkl",edinburgh_user_list)
	Yelp_save_list("edinburgh_user_info.pkl",edinburgh_user_info)
	Yelp_save_dict("edinburgh_review.json",edinburgh_review)
	Yelp_save_dict("edinburgh_user_rating_dict.json",edinburgh_user_rating_dict)
	Yelp_save_dict("edinburgh_item_rating_dict.json",edinburgh_item_rating_dict)
	Yelp_save_list("edinburgh_new_rating_list.pkl",new_rating_list)
	




