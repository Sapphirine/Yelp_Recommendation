//
//  OldUserFilterViewController.h
//  YelpRecommendation
//
//  Created by Yi Wu on 12/22/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface OldUserFilterViewController : UIViewController<UIPickerViewDataSource,UIPickerViewDelegate>

@property (strong, nonatomic) IBOutlet UILabel *label;

@property (weak, nonatomic) NSString *textContent;

@property (weak, nonatomic) IBOutlet UIPickerView *cityfilter;

@end
