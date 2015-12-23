//
//  ViewController.m
//  YelpRecommendation
//
//  Created by Yi Wu on 12/13/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import "ViewController.h"
#import "OldUserFilterViewController.h"

@interface ViewController ()

@end

@implementation ViewController



-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender{
    if([segue.identifier isEqualToString:@"old1"]){
        OldUserFilterViewController *controller = (OldUserFilterViewController *)segue.destinationViewController;
        controller.textContent = self.userIDfield.text;
    }
}


- (void)viewDidLoad {
    [super viewDidLoad];
    

    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}






@end
