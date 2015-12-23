//
//  NewUserFilterViewController.h
//  YelpRecommendation
//
//  Created by Yi Wu on 12/15/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface NewUserFilterViewController : UIViewController<UIPickerViewDataSource,UIPickerViewDelegate>

@property (weak, nonatomic) IBOutlet UIPickerView *cityfilter;


- (IBAction)getList:(id)sender;

@end
