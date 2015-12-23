//
//  OldUserFilterViewController.m
//  YelpRecommendation
//
//  Created by Yi Wu on 12/22/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import "OldUserFilterViewController.h"
#import "OldUserListViewController.h"

@interface OldUserFilterViewController () {
    
    NSArray *cityArray;
    NSString *selectedCity;
    
}

@end

@implementation OldUserFilterViewController

@synthesize cityfilter;

-(void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender{
    if([segue.identifier isEqualToString:@"old2"]){
        OldUserListViewController *controller = (OldUserListViewController *)segue.destinationViewController;
        controller.textContent2 = self.textContent;
        controller.textCity = selectedCity;
    }
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
    cityArray = [[NSArray alloc]initWithObjects:@"Madison",@"Pittsburgh",@"Edinburgh", nil];
    selectedCity = @"Madison";
    
    NSString *string1 = @"Welcome, ";
    self.label.text = [[string1 stringByAppendingString:self.textContent] stringByAppendingString:@"!"];
 // self.label.text = self.textContent;
    
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