//
//  NewUserListViewController.m
//  YelpRecommendation
//
//  Created by Yi Wu on 12/17/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import "NewUserListViewController.h"

@interface NewUserListViewController ()

@end

@implementation NewUserListViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.

/*    if ([self.textCity isEqualToString: @"Madison"]){
        self.restaurantList = @[@"Talula", @"TGI Friday's", @"Panchero's Mexican Grill", @"Erin's Snug Irish Pub", @"Shish Cafe Inc", @"Athens Gyros", @"Kfc", @"Dotty Dumpling's Dowry", @"Domino's Pizza", @"Maharaja Restaurant"];
        self.addressList = @[@"802 Atlas AveMadison, WI 53714", @"2502 East Springs DrMadison, WI 53704", @"402 S Gammon RdMadison, WI 53719", @"4601 American PkwyMadison, WI 53718", @"5510 University AveSpring HarborMadison, WI 53705", @"1614 Monroe StDudgeon-MonroeMadison, WI 53711", @"7501 Mineral Point RdMadison, WI 53717", @"317 N Frances StCapitolMadison, WI 53703", @"409 W Gorham StCapitolMadison, WI 53703", @"1707 Thierer RdMadison, WI 53704"];
    }
    else if ([self.textCity isEqualToString: @"Las Vegas"]){
        self.restaurantList = @[@"Gates & Brovi", @"Surco Peruvian Cuisine", @"Lava Lounge", @"Vientiane Restaurant", @"Sushi Express", @"Capriotti's Sandwich Shop", @"Osaka House", @"Bruegger's Bagels", @"Glass Nickel Pizza", @"Antojitos el Toril"];
        self.addressList = @[@"3502 Monroe StDudgeon-MonroeMadison, WI 53711", @"515 Cottage Grove RdLake EdgeMadison, WI 53716", @"461 W Gilman StCapitolMadison, WI 53703", @"626 S Park StGreenbushMadison, WI 53715", @"610 University AveCapitolMadison, WI 53715", @"902 Regent StSte BSouth CampusMadison, WI 53715", @"505 State StCapitolMadison, WI 53703", @"6150 Mineral Point RdFaircrestMadison, WI 53705", @"5003 University AveMadison, WI 53705", @"515 Cottage Grove RdLake EdgeMadison, WI 53774"];
    }
    else {
        self.restaurantList = @[@"Fair Trade Coffee", @"Lava Lounge", @"Cousins Subs", @"608 Restaurant and Bar", @"People's Bakery", @"Slice's Bar & Grill", @"Dahmen's Pizza Place", @"Rocky Rococo Pan Style Pizza", @"Eagle Crest Bar", @"Bourbon Street Grille"];
        self.addressList = @[@"418 State StCapitolMadison, WI 53703", @"461 W Gilman StCapitolMadison, WI 53703", @"3715 E Washington AveMayfair ParkMadison, WI 53704", @"212 State StCapitolMadison, WI 53703", @"2810 E Washington AveEken ParkMadison, WI 53704", @"2417 Pennsylvania AveEmerson EastMadison, WI 53704", @"6654 Mineral Point RdMadison, WI 53705", @"7952 Tree LnOakbridge CommunityMadison, WI 53717", @"3710 County Rd TRidgewoodMadison, WI 53704", @"6312 Metropolitan LnMadison, WI 53713"];
    } */
    
    void (^selectedCase)() = @{
                               @"Madison" : ^{
                                   self.restaurantList = @[@"Kakilima Food Cart", @"Kerol's Kitchen", @"Old Market Bistro", @"Noodle Express", @"Lake Vista Cafe", @"Madison Food Explorers", @"Library Mall", @"Ladonia Cafe", @"Zen Sushi", @"Taco Bell"];
                                   self.addressList = @[@"Library MallCapitolMadison, WI 53703", @"Tenney - LaphamMadison, WI 53703", @"15 N Butler StCapitolMadison, WI 53703", @"2817 E Washington AveStarkweather - YaharMadison, WI 53704", @"One John Nolen DrCapitolMadison, WI 53703", @"2406 Upham StCapitolMadison, WI 53704", @"728 State StCapitolMadison, WI 53706", @"Mifflin and PinckneyCapitolMadison, WI 53703", @"700 State StCapitolMadison, WI 53706", @"1920 S Park StBram's AdditionMadison, WI 53713"];
                               },
                               @"Pittsburgh" : ^{
                                   self.restaurantList = @[@"Sam's Sun Sandwich", @"Rudy Martino Original House of Submarines", @"Azure Cafe & Grill", @"Hog's Head Bar and Grill", @"Rocky's II", @"Popeyes", @"Juice Up 412", @"XO Cafe & Lounge", @"Red Hot Pittsburgh", @"Pizza Vespucci"];
                                   self.addressList = @[@"2616 Brownsville RdCarrickPittsburgh, PA 15227", @"1918 Monongahela AvePittsburgh, PA 15218", @"565 Lincoln AveBellevuePittsburgh, PA 15202", @"3433 Spring Garden AveWest ViewPittsburgh, PA 15212", @"1562 Island AveNorth SidePittsburgh, PA 15233", @"1000 Pitt StPittsburgh, PA 15221", @"124 S Highland AveEast LibertyPittsburgh, PA 15206", @"47 Bates StOaklandPittsburgh, PA 15213", @"Corner of Grant & OliverDowntownPittsburgh, PA 15219", @"1710 Forbes AveThe Hill DistrictPittsburgh, PA 15219"];
                               },
                               @"Edinburgh" : ^{
                                   self.restaurantList = @[@"Patisserie Madeleine", @"Hernandez & Co", @"Dante's Restaurant", @"Skippers Bistro", @"Hadrians Brasserie", @"Ravenous", @"Cinnamon", @"Nonna's Kitchen", @"Thyme", @"B&D's Kitchen"];
                                   self.addressList = @[@"27b Raeburn PlaceStockbridgeEdinburgh EH4 1HU", @"31a Queensferry StreetNew TownEdinburgh EH2 4QS", @"48/50 Bridge RoadEdinburgh EH13 0LQ", @"1a Dock PlaceLeithEdinburgh EH6 6LU", @"1 Princes StreetThe Balmoral HotelOld TownEdinburgh", @"12 Raeburn PlaceStockbridgeStockbridgeEdinburgh EH4", @"249 Portobello High StreetEdinburgh EH15 2AW", @"45 Morningside RoadBruntsfieldEdinburgh EH10 4AZ", @"44 Earl Grey StreetTollcrossTollcrossEdinburgh EH3 9BN", @"214 dalry roadHaymarketEdinburgh EH11 2ES"];
                               },
                               }[self.textCity];
    
    if (selectedCase != nil)
        selectedCase();
    
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return [self.restaurantList count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    NSString *SimpleIdentifier = @"SimpleIdentifier";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:SimpleIdentifier];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:SimpleIdentifier];
    }
    
    cell.textLabel.text = self.restaurantList[indexPath.row];
    cell.detailTextLabel.text = self.addressList[indexPath.row];
    cell.textLabel.font = [UIFont boldSystemFontOfSize:20];
    
    UIImage *image1 = [UIImage imageNamed:@"Cartoon-Restaurant.png"];
    cell.imageView.image = image1;
    
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath {
    return 60;
}


- (NSIndexPath *)tableView:(UITableView *)tableView willSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    
    return indexPath;
}


- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(nonnull NSIndexPath *)indexPath {
    
    NSString *rowValue = self.restaurantList[indexPath.row];
    NSString *message0 = [[NSString alloc] initWithFormat:@"%@",rowValue];
    NSString *message1 = [[NSString alloc] initWithFormat:@"Address: %@",self.addressList[indexPath.row]];
    
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:message0 message:message1 delegate:nil cancelButtonTitle:@"Cool" otherButtonTitles:nil, nil];
    
    [alert show];
    
    [tableView deselectRowAtIndexPath:indexPath animated:YES];
    
}


/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
