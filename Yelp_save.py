from __future__ import with_statement
from Yelp_get import Yelp_get
from Yelp_data import Yelp_data
import json
import gc
import pickle
import csv

def Yelp_save_list(list_path,file_name):
	with open(list_path,"wb") as file:
		pickle.dump(file_name,file)
	file.close()

def Yelp_reload_list(list_path):
	with open(list_path,"rb") as file:
		list_file = pickle.load(file)
	file.close()
	return list_file

def Yelp_save_dict(dict_path,file_name):
	with open(dict_path,"wb") as file:
		json.dump(file_name,file)
	file.close()

def Yelp_reload_dict(dict_path):
	with open(dict_path,"rb") as file:
		dict_file = json.load(file)
	file.close()
	return dict_file

def Yelp_save_csv(csv_path,file_name):
	with open(csv_path,"wb") as file:
		writer = writer=csv.writer(file)
		for item in file_name:
			if (type(item) is list):
				writer.writerows([item])
			else:
				writer.writerow([item])
	file.close()


if __name__ == "__main__":
	user_path = "yelp_academic_dataset_user.json"				
	review_path = "yelp_academic_dataset_review.json"
	business_path = "yelp_academic_dataset_business.json"
	path = [user_path,review_path,business_path]
	yelp = Yelp_get(path)
	user = yelp.get_user()
	Yelp_save.Yelp_save_dict("user.json",user)
	user.clear()

	business = yelp.get_business()
	Yelp_save.Yelp_save_dict("business.json",business)
	restaurant = Yelp_data.get_restaurant(business)
	Yelp_save_dict("restaurant.json",restaurant)
	
	restaurant_id_list = Yelp_data.get_restaurant_id_from_business(business)
	business.clear()

	review = yelp.get_review()
	Yelp_save.Yelp_save_dict("review.json",review)
	
	review_restaurant = Yelp_data.get_restaurant_review(restaurant_id_list,review)
	Yelp_save.Yelp_save_dict("review_restaurant.json",review_restaurant)
	
	review.clear()
	review_restaurant.clear()














