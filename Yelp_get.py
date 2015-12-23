from __future__ import with_statement
import json
import sys
import Yelp_data

reload(sys)
sys.setdefaultencoding("utf-8")

class Yelp_get(object):

    """docstring for get_Yelp"""

    """ get user information from user data set """

    """
    return user data features:
    user_id,name,yelping_since,votes_funny,votes_useful,votes_cool,
    elite,fans,average_stars,review_count,friend

    """
    def get_user(self):
        user_path = self.path[0]
        user = {}
        with open(user_path) as file:
            for line in file:
                temp_data = json.loads(line.encode("utf-8"))
                user[temp_data["user_id"]] = {}
                user[temp_data["user_id"]]["name"] = str(temp_data["name"])
                user[temp_data["user_id"]]["yelping_since"] = temp_data["yelping_since"]
                user[temp_data["user_id"]]["votes_funny"] = temp_data["votes"]["funny"]
                user[temp_data["user_id"]]["votes_useful"] = temp_data["votes"]["useful"]
                user[temp_data["user_id"]]["votes_cool"] = temp_data["votes"]["cool"]
                user[temp_data["user_id"]]["elite"] = temp_data["elite"]
                user[temp_data["user_id"]]["fans"] = temp_data["fans"]
                user[temp_data["user_id"]]["average_stars"] = temp_data["average_stars"]
                user[temp_data["user_id"]]["review_count"] = temp_data["review_count"]
                user[temp_data["user_id"]]["friends"] = [str(friend) for friend in temp_data["friends"]]
        file.close()
        return user


    """ get review from review data set """
    """
    return review data features:

    user_id,business_id,votes_funny,votes_useful,votes_cool,stars,date,text

    """

    def get_review(self):
        review_path = self.path[1]
        review = {}
        #i=1
        with open(review_path) as file:
            for line in file:
                #i+=1
                temp_data = json.loads(line.encode("utf-8"))
                
                review[temp_data["review_id"]]={}
                review[temp_data["review_id"]]["user_id"] = str(temp_data["user_id"])
                review[temp_data["review_id"]]["business_id"] = str(temp_data["business_id"])
                review[temp_data["review_id"]]["votes_funny"] = temp_data["votes"]["funny"]
                review[temp_data["review_id"]]["votes_useful"] = temp_data["votes"]["useful"]
                review[temp_data["review_id"]]["votes_cool"] = temp_data["votes"]["cool"]
                review[temp_data["review_id"]]["stars"] = temp_data["stars"]
                review[temp_data["review_id"]]["date"] = str(temp_data["date"])
                review[temp_data["review_id"]]["text"] = str(temp_data["text"]).replace("\n","")
                
        file.close()
        return review


    """ get business information from business data set """
    """
    return business data features:
    full_address, categories, city, review_count, name, 
    longitude, state, stars, latitude, attributes
    
    """

    def get_business(self):
        business_path = self.path[2]
        business = {}
        #i=0
        with open(business_path) as file:
            for line in file:
                #i+=1
                temp_data = json.loads(line.encode("utf-8"))
                business[temp_data["business_id"]] = {}
                business[temp_data["business_id"]]["full_address"] = str(temp_data["full_address"]).replace("\n","")
                business[temp_data["business_id"]]["categories"] = [str(item) for item in temp_data["categories"]]
                business[temp_data["business_id"]]["city"] = temp_data["city"]
                business[temp_data["business_id"]]["review_count"] = temp_data["review_count"]
                business[temp_data["business_id"]]["name"] = temp_data["name"]
                business[temp_data["business_id"]]["longitude"] = temp_data["longitude"]
                business[temp_data["business_id"]]["state"] = temp_data["state"]
                business[temp_data["business_id"]]["stars"] = temp_data["stars"]
                business[temp_data["business_id"]]["latitude"] = temp_data["latitude"]
                business[temp_data["business_id"]]["attributes"] = [[str(items) for items in item] for item in temp_data["attributes"].items()]
                
        file.close()
        return business#,restaurants



    def __init__(self, path):
        super(Yelp_get, self).__init__()
        self.path = path




