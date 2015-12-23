# Yelp_Recommendation  
_____________________
This contains the personalized recommendation systems code based on Yelp data. 

Author: 
- Qianbo Wang    
uni: qw2180    
- Yi Wu    
uni: yw2682    
- Zuyi Wu      
uni: zw2289    

_____________________

## Data Processing    
We download the data from Yelp Challenge Data Set: [https://www.yelp.com/dataset_challenge/dataset](https://www.yelp.com/dataset_challenge/dataset)
- Yelp_get.py contains the class of get and parse data from json file and static methods within the Yelp_get class    
- Yelp_data.py contains the class of Yelp data file, with static methods of retrieving the specific features and information    
- Yelp_save.py contains the methods for save and reload the data files    

_____________________
## Recommend Algorithm    
- Yelp_recommender.py contains the class of recommendation with methods of main mix collaborative filtering algorithm    
- Yelp_main.py is the main code for building recommendation system    
- Review_functions.py, Review_main, and tfidf contain the review analysis for Yelp data and get user scores from past reviews    

_____________________
## Specific City Recommendation    
- Yelp_Edinburgh.py contains the data processing and making recommendations for Edinburgh users    
- Yelp_Pittsburgh.py contains the data processing and making recommendations for Pittsburgh users    
- Yelp_Madison.py contains the data processing and making recommendations for Madison users    

______________________
# Description for running code

1. First, download the data from the [Yelp data set](https://www.yelp.com/dataset_challenge/dataset).    
2. Second, run Yelp_get.py to parse the data.
3. Third, run Yelp_save.py to save the data into another json,pickle and csv files
4. Fourth, run Yelp_Madison.py, Yelp_Pittsburgh.py and run Yelp_Edinburgh.py to get restaurants and users and also their past ratings for these specific cities.
5. Finally, run Yelp_main.py, and combine the scores given by mix collaborative filtering algorithm and review analysis to calculate the final score for users and make recommendations for users.
6. Then use iOS projects (objective-c) code to build the application.
