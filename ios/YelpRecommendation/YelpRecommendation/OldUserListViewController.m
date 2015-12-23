//
//  OldUserListViewController.m
//  YelpRecommendation
//
//  Created by Yi Wu on 12/22/15.
//  Copyright © 2015 Qianbo Wang, Yi Wu, Zuyi Wu. All rights reserved.
//

#import "OldUserListViewController.h"

@interface OldUserListViewController ()

@end

@implementation OldUserListViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    
    if ([self.textCity isEqualToString: @"Madison"]){
     
        self.restaurantList = @[@"Kakilima Food Cart", @"Kerol's Kitchen", @"Old Market Bistro", @"Noodle Express", @"Lake Vista Cafe", @"Madison Food Explorers", @"Library Mall", @"Ladonia Cafe", @"Zen Sushi", @"Taco Bell"];
        self.addressList = @[@"Library MallCapitolMadison, WI 53703", @"Tenney - LaphamMadison, WI 53703", @"15 N Butler StCapitolMadison, WI 53703", @"2817 E Washington AveStarkweather - YaharMadison, WI 53704", @"One John Nolen DrCapitolMadison, WI 53703", @"2406 Upham StCapitolMadison, WI 53704", @"728 State StCapitolMadison, WI 53706", @"Mifflin and PinckneyCapitolMadison, WI 53703", @"700 State StCapitolMadison, WI 53706", @"1920 S Park StBram's AdditionMadison, WI 53713"];
        
        void (^selectedCase)() = @{
                               @"epNQpw" : ^{
                                   self.restaurantList = @[@"Ground Zero", @"Talula", @"Basie's", @"Espresso Royale Caffe", @"Domino's Pizza", @"QQ Asian Buffet", @"Luigi's", @"Tienda Los Gemelos", @"Tempest Oyster Bar", @"Ingrid's Lunch Box"];
                                   self.addressList = @[@"744 Williamson StWilliamson - MarquetteMadison, WI 53703", @"802 Atlas AveMadison, WI 53714", @"517 Grand Canyon DrMadison, WI 53719", @"208 State StCapitolMadison, WI 53703", @"409 W Gorham StCapitolMadison, WI 53703", @"1291 N Sherman AveMadison, WI 53704", @"515 S Midvale BlvdWestmorlandMadison, WI 53711", @"6713 Odana RdSte 8Madison, WI 53719", @"120 E Wilson StCapitolMadison, WI 53703", @"State StCapitolMadison, WI 53703"];
                               },
                               @"WvdnCw" : ^{
                                   self.restaurantList = @[@"Talula", @"TGI Friday's", @"Panchero's Mexican Grill", @"Erin's Snug Irish Pub", @"Shish Cafe Inc", @"Athens Gyros", @"Kfc", @"Dotty Dumpling's Dowry", @"Domino's Pizza", @"Maharaja Restaurant"];
                                   self.addressList = @[@"802 Atlas AveMadison, WI 53714", @"2502 East Springs DrMadison, WI 53704", @"402 S Gammon RdMadison, WI 53719", @"4601 American PkwyMadison, WI 53718", @"5510 University AveSpring HarborMadison, WI 53705", @"1614 Monroe StDudgeon-MonroeMadison, WI 53711", @"7501 Mineral Point RdMadison, WI 53717", @"317 N Frances StCapitolMadison, WI 53703", @"409 W Gorham StCapitolMadison, WI 53703", @"1707 Thierer RdMadison, WI 53704"];
                               },
                               @"BzWXkw" : ^{
                                   self.restaurantList = @[@"Gates & Brovi", @"Surco Peruvian Cuisine", @"Lava Lounge", @"Vientiane Restaurant", @"Sushi Express", @"Capriotti's Sandwich Shop", @"Osaka House", @"Bruegger's Bagels", @"Glass Nickel Pizza", @"Antojitos el Toril"];
                                   self.addressList = @[@"3502 Monroe StDudgeon-MonroeMadison, WI 53711", @"515 Cottage Grove RdLake EdgeMadison, WI 53716", @"461 W Gilman StCapitolMadison, WI 53703", @"626 S Park StGreenbushMadison, WI 53715", @"610 University AveCapitolMadison, WI 53715", @"902 Regent StSte BSouth CampusMadison, WI 53715", @"505 State StCapitolMadison, WI 53703", @"6150 Mineral Point RdFaircrestMadison, WI 53705", @"5003 University AveMadison, WI 53705", @"515 Cottage Grove RdLake EdgeMadison, WI 53774"];
                               },
                               }[self.textContent2];
    
        if (selectedCase != nil)
            selectedCase();
        }
    
    
    if ([self.textCity isEqualToString: @"Pittsburgh"]){
        
        self.restaurantList = @[@"Sam's Sun Sandwich", @"Rudy Martino Original House of Submarines", @"Azure Cafe & Grill", @"Hog's Head Bar and Grill", @"Rocky's II", @"Popeyes", @"Juice Up 412", @"XO Cafe & Lounge", @"Red Hot Pittsburgh", @"Pizza Vespucci"];
        self.addressList = @[@"2616 Brownsville RdCarrickPittsburgh, PA 15227", @"1918 Monongahela AvePittsburgh, PA 15218", @"565 Lincoln AveBellevuePittsburgh, PA 15202", @"3433 Spring Garden AveWest ViewPittsburgh, PA 15212", @"1562 Island AveNorth SidePittsburgh, PA 15233", @"1000 Pitt StPittsburgh, PA 15221", @"124 S Highland AveEast LibertyPittsburgh, PA 15206", @"47 Bates StOaklandPittsburgh, PA 15213", @"Corner of Grant & OliverDowntownPittsburgh, PA 15219", @"1710 Forbes AveThe Hill DistrictPittsburgh, PA 15219"];
        
        void (^selectedCase)() = @{
                                   @"sOYR4A" : ^{
                                       self.restaurantList = @[@"The Dream BBQ", @"Melange Bistro Bar", @"The Zenith", @"Sports Rock Cafe", @"PLUM pan asian kitchen", @"Jerome Bettis Grille 36", @"Island Cafe", @"Emilia Romagna", @"Qdoba Mexican Grill", @"Sawasdee Thai Kitchen"];
                                       self.addressList = @[@"7600 N Braddock AveHomewoodPittsburgh, PA 15208", @"136 6th StDowntownPittsburgh, PA 15222", @"86 S 26th StSouth SidePittsburgh, PA 15203", @"1400 Smallman StStrip DistrictPittsburgh, PA 15222", @"5996 Penn Cir SShadysidePittsburgh, PA 15206", @"393 N Shore DrNorth SidePittsburgh, PA 15212", @"224 Bessemer CtSouth SidePittsburgh, PA 15219", @"108 19th StStrip DistrictPittsburgh, PA 15222", @"1028 Freeport RdPittsburgh, PA 15238", @"112 Abbeyville RdPittsburgh, PA 15228"];
                                   },
                                   @"vCiCqA" : ^{
                                       self.restaurantList = @[@"Melange Bistro Bar", @"The Dream BBQ", @"The Zenith", @"Sports Rock Cafe", @"PLUM pan asian kitchen", @"Jerome Bettis Grille 36", @"Emilia Romagna", @"Island Cafe", @"Qdoba Mexican Grill", @"Sawasdee Thai Kitchen"];
                                       self.addressList = @[@"136 6th StDowntownPittsburgh, PA 15222", @"7600 N Braddock AveHomewoodPittsburgh, PA 15208", @"86 S 26th StSouth SidePittsburgh, PA 15203", @"1400 Smallman StStrip DistrictPittsburgh, PA 15222", @"5996 Penn Cir SShadysidePittsburgh, PA 15206", @"393 N Shore DrNorth SidePittsburgh, PA 15212", @"108 19th StStrip DistrictPittsburgh, PA 15222", @"224 Bessemer CtSouth SidePittsburgh, PA 15219", @"1028 Freeport RdPittsburgh, PA 15238", @"112 Abbeyville RdPittsburgh, PA 15228"];
                                   },
                                   @"MfAzTg" : ^{
                                       self.restaurantList = @[@"The Dream BBQ", @"Melange Bistro Bar", @"The Zenith", @"Sports Rock Cafe", @"PLUM pan asian kitchen", @"Jerome Bettis Grille 36", @"Emilia Romagna", @"Island Cafe", @"Qdoba Mexican Grill", @"Sawasdee Thai Kitchen"];
                                       self.addressList = @[@"7600 N Braddock AveHomewoodPittsburgh, PA 15208", @"136 6th StDowntownPittsburgh, PA 15222", @"86 S 26th StSouth SidePittsburgh, PA 15203", @"1400 Smallman StStrip DistrictPittsburgh, PA 15222", @"5996 Penn Cir SShadysidePittsburgh, PA 15206", @"393 N Shore DrNorth SidePittsburgh, PA 15212", @"108 19th StStrip DistrictPittsburgh, PA 15222", @"224 Bessemer CtSouth SidePittsburgh, PA 15219", @"1028 Freeport RdPittsburgh, PA 15238", @"112 Abbeyville RdPittsburgh, PA 15228"];
                                   },
                                   }[self.textContent2];
        
        if (selectedCase != nil)
            selectedCase();
    }
    
    
    
    
    if ([self.textCity isEqualToString: @"Edinburgh"]){
        
        self.restaurantList = @[@"Patisserie Madeleine", @"Hernandez & Co", @"Dante's Restaurant", @"Skippers Bistro", @"Hadrians Brasserie", @"Ravenous", @"Cinnamon", @"Nonna's Kitchen", @"Thyme", @"B&D's Kitchen"];
        self.addressList = @[@"27b Raeburn PlaceStockbridgeEdinburgh EH4 1HU", @"31a Queensferry StreetNew TownEdinburgh EH2 4QS", @"48/50 Bridge RoadEdinburgh EH13 0LQ", @"1a Dock PlaceLeithEdinburgh EH6 6LU", @"1 Princes StreetThe Balmoral HotelOld TownEdinburgh", @"12 Raeburn PlaceStockbridgeStockbridgeEdinburgh EH4", @"249 Portobello High StreetEdinburgh EH15 2AW", @"45 Morningside RoadBruntsfieldEdinburgh EH10 4AZ", @"44 Earl Grey StreetTollcrossTollcrossEdinburgh EH3 9BN", @"214 dalry roadHaymarketEdinburgh EH11 2ES"];
        
        void (^selectedCase)() = @{
                                   @"3Ql8CQ" : ^{
                                       self.restaurantList = @[@"Teuchters Landing", @"Zizzi", @"Parliament House Hotel", @"Marchmont Takeaway", @"The Dome", @"The Orchard", @"Locanda de Gusti", @"Mintleaf", @"Pep & Fodder", @"The Cholas"];
                                       self.addressList = @[@"1a and 1c Dock PlaceLeithLeithEdinburgh EH6 6LU", @"Ocean TerminalFood TerraceLeithEdinburgh EH6 6JJ", @"15 Calton HillEdinburgh EH1 3BJ", @"98 Marchmont RoadMarchmontEdinburgh EH9 1HR", @"14 George StreetNew TownEdinburgh EH2 2PF", @"1-2 Howard PlaceStockbridgeEdinburgh EH3 5JZ", @"102 Dalry RoadWest EndEdinburgh EH11 2DW", @"28 Bernard StreetLeithEdinburgh EH6 6PP", @"11 Waterloo PlaceEdinburgh EH1", @"63 Clerk StreetNewingtonEdinburgh EH8 9JQ"];
                                   },
                                   @"sHxZug" : ^{
                                       self.restaurantList = @[@"9 Cellars", @"Lian Pu", @"CaffeLatte", @"Wee Bite", @"Blackcherry Cafe", @"The Original Coffee Bean", @"Omar Khayyam", @"Ocean Spice", @"Toast", @"Kismot"];
                                       self.addressList = @[@"1-3 York PlaceNew TownEdinburgh EH2 1", @"14 Marshall StreetNewingtonEdinburgh EH8 9BU", @"1A Logie Green RoadCanonmillsCannonmillsEdinburgh EH7 4EY", @"Saint Mary's StreetNewingtonEdinburgh EH8 8", @"29 GrassmarketGrassmarketEdinburgh EH1 2HS", @"5-7 Station RoadEdinburgh EH12 7AA", @"1 Grosvenor StreetWest EndEdinburgh EH12 5ED", @"AnnfieldLeithEdinburgh EH6 4JF", @"146 Marchmont RoadMarchmontEdinburgh EH9 1AQ", @"29 St Leonard's StreetNewingtonEdinburgh EH8 9QN"];
                                   },
                                   @"yA4b-Q" : ^{
                                       self.restaurantList = @[@"Spud U Like", @"Lian Pu", @"Slug & Lettuce", @"Hanam's", @"Tonic", @"I-Ching", @"10-to-10 In Delhi", @"Bar Napoli", @"Bar Kohl", @"Silver Bowl"];
                                       self.addressList = @[@"Princes MallPrinces StreetNew TownEdinburgh EH2 2AN", @"14 Marshall StreetNewingtonEdinburgh EH8 9BU", @"Unit 8 Omni CtrGreenside PlNew TownEdinburgh EH1 3BN", @"3 Johnston TerraceOld TownEdinburgh EH1 2PW", @"34a North Castle StreetNew TownEdinburgh EH2 3BN", @"83 Slateford RoadEdinburgh EH11 1QR", @"67 Nicolson StreetNewingtonEdinburgh EH8 9BZ", @"75 Hanover StreetNew TownEdinburgh EH2 1EE", @"54 George IV BridgeOld TownEdinburgh EH1 1EJ", @"311 Leith WalkLeithEdinburgh EH6 8SA"];
                                   },
                                   }[self.textContent2];
        
        if (selectedCase != nil)
            selectedCase();
    }

    
    
    
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
