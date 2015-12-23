//
//  OldUserListViewController.h
//  YelpRecommendation
//
//  Created by Yi Wu on 12/22/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface OldUserListViewController : UIViewController<UITableViewDataSource,UITableViewDelegate>

@property (weak, nonatomic) NSString *textContent2;
@property (weak, nonatomic) NSString *textCity;

@property (copy, nonatomic) NSArray *restaurantList;
@property (copy, nonatomic) NSArray *addressList;

@end


