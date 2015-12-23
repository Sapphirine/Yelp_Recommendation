//
//  NewUserFilterViewController.m
//  YelpRecommendation
//
//  Created by Yi Wu on 12/15/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import "NewUserFilterViewController.h"
#import "NewUserListViewController.h"

@interface NewUserFilterViewController () {
    
    NSArray *cityArray;
    NSString *selectedCity;
}

@end

@implementation NewUserFilterViewController

@synthesize cityfilter;

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    cityArray = [[NSArray alloc]initWithObjects:@"Madison",@"Pittsburgh",@"Edinburgh", nil];
    selectedCity = @"Madison";
}


-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender{
    if([segue.identifier isEqualToString:@"new2"]){
        NewUserListViewController *controller = (NewUserListViewController *)segue.destinationViewController;
        controller.textCity = selectedCity;
        
    }
}


- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView{
    
    return 1;
    
}

- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component{
    
    return cityArray.count;
    
}


- (NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component{
    
    return [cityArray objectAtIndex:row];
    

}


- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component {
    
    selectedCity = [cityArray objectAtIndex:row];
    
}




- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

- (IBAction)getList:(id)sender {
}
@end
