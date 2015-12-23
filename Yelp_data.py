
class Yelp_data(object):
	"""docstring for Yelp_data"""
	
	""" retrieve user_id list of all user_id """
	@staticmethod
	def get_user_list(user):       
		return user.keys()

	""" retrieve user information for given user_id from user data """
	@staticmethod
	def get_user_from_id(user_id,user):
		if user_id in user.keys():
			return user[user_id]
		else:
			return {}
	""" retrieve user_id list from review data """
	@staticmethod
	def get_review_user_list(review):
		all_user = [review[review_id]["user_id"] for review_id in review.keys()] 
		return list(set(all_user))


	""" retrieve business_id list from review data """
	@staticmethod
	def get_review_business_list(review):
		all_business = [review[review_id]["business_id"] for review_id in review.keys()] 
		return list(set(all_business))


	""" retrieve review content for given review_id """ 
	@staticmethod
	def get_review_from_id(review_id,review):
		if review_id in review.keys():
			return review[review_id]
		else:
			return {}
    
	""" retrieve all reviews for given user_id """
	@staticmethod
	def get_review_from_user(user_id,review):
		review_id_list = review.keys()
		review_all_user = [review[review_id]["user_id"] for review_id in review_id_list]
		if user_id in review_all_user:
			all_review = {}
			indices = [index for index, user in enumerate(review_all_user) if user == user_id]
			for num in range(len(indices)):
				business_id = review[review_id_list[indices[num]]]["business_id"]
				all_review[business_id] = review[review_id_list[indices[num]]]
			return all_review
		else:
			return {}

	""" retrieve all review stars for given user_id """
	@staticmethod
	def get_review_stars_from_user(user_id,review):
		review_id_list = review.keys()
		review_all_user = [review[review_id]["user_id"] for review_id in review_id_list]
		if user_id in review_all_user:
			all_review = {}
			indices = [index for index, user in enumerate(review_all_user) if user == user_id]
			for num in range(len(indices)):
				business_id = review[review_id_list[indices[num]]]["business_id"]
				all_review[business_id] = review[review_id_list[indices[num]]]["stars"]
			return all_review
		else:
			return {}
	
	""" retrieve all review_id for given user_id """
	@staticmethod
	def get_review_from_user(user_id,review):
		review_id_list = review.keys()
		review_all_user = [review[review_id]["user_id"] for review_id in review_id_list]
		if user_id in review_all_user:
			indices = [index for index, user in enumerate(review_all_user) if user == user_id]
			review_id = [review_id_list[indices[num]] for num in range(len(indices))] 
			return review_id
		else:
			return []

	""" retrieve all reviews for given business_id """
	@staticmethod
	def get_review_from_business(business_id,review):
		review_id_list = review.keys()
		review_all_business = [review[review_id]["business_id"] for review_id in review_id_list]
		if user_id in review_all_business:
			all_review = {}
			indices = [index for index, business in enumerate(review_all_business) if business == business_id]
			for num in range(len(indices)):
				user_id = review[review_id_list[indices[num]]]["user_id"]
				all_review[user_id] = review[review_id_list[indices[num]]]
			return all_review
		else:
			return {}

	""" retrieve review content for given review_id """
	@staticmethod
	def get_review_from_id(review_id,review):
		if review_id in review.keys():
			return review[review_id]
		else:
			return {}


	""" retrieve business name for given business_id """
	@staticmethod
	def get_business_from_id(business_id,business):
		if business_id in business.keys():
			return business[business_id]["name"]
		else:
			return business_id

	""" retrieve business information for given business_id """
	@staticmethod
	def get_business_from_id(business_id,business):
		if business_id in business.keys():
			return business[business_id]
		else:
			return {}

	""" retrieve business city list from business data """
	@staticmethod
	def get_business_city(business):
		all_city = [str(business[business_id]["city"]) for business_id in business.keys()] 
		return list(set(all_city))

	""" retrieve all restaurants info for given city """
	@staticmethod
	def get_business_from_city(city,business):
		business_id_list = business.keys()
		business_all_city = [business[business_id]["city"] for business_id in business_id_list]
		if city in business_all_city:
			indices = [index for index, city_id in enumerate(business_all_city) if city_id == city]
			business_id = [business_id_list[indices[num]] for num in range(len(indices))]
			return business_id 
		else:
			return []

	""" retrieve all restaurant_id from business data """
	@staticmethod
	def get_restaurant_id_from_business(business):
		business_id_list = business.keys()
		categories_list = [business[business_id]["categories"] for business_id in business_id_list]
		indices = [index for index, category in enumerate(categories_list) if ('Restaurants' in category)]
		restaurant_list = [business_id_list[indices[num]] for num in range(len(indices))]
		return restaurant_list

	""" retrieve all restaurant info from business data """
	@staticmethod
	def get_restaurant(business):
		business_id_list = business.keys()
		categories_list = [business[business_id]["categories"] for business_id in business_id_list]
		indices = [index for index, category in enumerate(categories_list) if ('Restaurants' in category)]
		restaurant = {}
		for num in range(len(indices)):
			restaurant[business_id_list[indices[num]]]=business[business_id_list[indices[num]]]
		return restaurant
    
	@staticmethod
	def get_restaurant_review(restaurant_id_list,review):
		review_restaurant = {}
		for review_id in review.keys():
			if review[review_id]["business_id"] in restaurant_id_list:
				review_restaurant[review_id] = review[review_id]
		return review_restaurant

	@staticmethod
	def get_user_list_from_review(review):

		user_list = [review[review_id]["user_id"] for review_id in review.keys()]
		return list(set(user_list))

	@staticmethod
	def get_business_list_from_review(review):
		business_list = [review[review_id]["business_id"] for review_id in review.keys()]
		return list(set(business_list))

	@staticmethod
	def get_restaurant_info(restaurant,restaurant_id):
		return restaurant[restaurant_id]

	@staticmethod
	def get_user_info(user,user_id):
		return user[user_id]
		
	@staticmethod
	def get_user_name(user,user_list):
		name_list = []
		for user_id in user_list:
			name.append(user[user_id]["name"])
		return name_list

	def __init__(self, user,review,business):
		super(data, self).__init__()
		self.user = user
		self.review = review
		self.business = business
		