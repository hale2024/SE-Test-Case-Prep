import csv
import unittest
import soccer_player
from soccer_player import Country
from soccer_player import Player

class TestSoccerFile(unittest.TestCase):
    def test_convert_csv_file_to_objects(self):
        all_countries=soccer_player.convert_csv_file_to_objects()
        for i in all_countries:
            if i.country_name=='Equatorial Guinea':
                result=i.player_list #Equatorial Guinea Team players
                break
        #case 1
        #checking if the name of players is returned correctly
        result1={i.name for i in result}
        Guinea_players={ 
                        'Akapo',
                        'José Machín',
                        'Iban Salvador',
                        'Pedro Obiang',
                        'C. Bejarano'
                        }
        self.assertSetEqual(result1, Guinea_players)
        #I tested whether the Equatorial Guinea players name list is the same as that of the player_list that is returned from our source code.
        #I also compared them as a set so that order of the players doesn't matter.

        #case #2
        #testing if the other attributes returned are being set properly
        for i in result:
            if i.name=='Akapo':
                result2=i
        self.assertEqual(result2.name, 'Akapo')
        self.assertEqual(result2.age, 25)
        self.assertEqual(result2.nationality, 'Equatorial Guinea')
        self.assertEqual(result2.overall, 70)
        self.assertEqual(result2.position, 'LB')

    def test_get_country_object_by_country_name(self):
        all_countries=soccer_player.convert_csv_file_to_objects()
        
        #case 1
        # testing for a country that doesn't exist
        a_negative_test=soccer_player.get_country_object_by_country_name(all_countries, 'Somalia')
        self.assertEqual(a_negative_test, 'No such country')
        #case 2
        # testing for a country that exists in the csv file
        a_positive_test=soccer_player.get_country_object_by_country_name(all_countries, 'Equatorial Guinea').player_list
        a_positive_test={i.name for i in a_positive_test}
        Guinea_players={'C. Bejarano','Akapo', 'José Machín', 'Iban Salvador', 'Pedro Obiang'}
        self.assertSetEqual(a_positive_test, Guinea_players)
        #I tested whether the Equatorial Guinea players list is the same as the player_list that is returned from our code.
        #I also compared them as a set so that order of the players doesn't matter.
    
    def test_player_creation(self):
        player_1=Player("Halleluyah", "21", "Ethiopia", "100", 'LW')
        self.assertEqual(player_1.name, "Halleluyah")
        self.assertEqual(player_1.age, 21) #checking if it the player class converts the age value inserted to an integer as it should
        self.assertEqual(player_1.nationality, "Ethiopia")
        self.assertEqual(player_1.overall, 100) #checking if it the player class converts the overall value inserted to an integer as it should
        self.assertEqual(player_1.position, 'LW')
        #I created a player named Halleluyah and checked if it was being created properly
    def test_player_comparision(self):
        #checking if comparision is made properly for players that have different overall rating
        player_1=Player("Halleluyah", 21, "Ethiopia", 100, 'LW')
        player_2=Player("Messi", 34, "Argentina", 56, 'FW')
        self.assertEqual(player_1>player_2, True)

        #checking if comparision is being made properly for players that have the same overall rating
        #since player_3 is the younger player he is the one favored
        player_3=Player("Halleluyah", 21, "Ethiopia", 100, 'LW')
        player_4=Player("Messi", 34, "Argentina", 100, 'FW')
        self.assertEqual(player_3>player_4, True)
    
    def test_player_string(self):
        player_1=Player("Halleluyah", 21, "Ethiopia", 100, 'LW')
        name_=str(player_1)
        self.assertEqual(name_, "Halleluyah")
        # I created a player object and converted the object to a string using str and verified if it returns the same name as I originally assigned it. 
    
    def test_player_repr(self):
        player_1=Player("Halleluyah", 21, "Ethiopia", 100, 'LW')
        name_=repr(player_1)
        self.assertEqual(name_, "Halleluyah, LW")
        # I created a player object and applied the repr method on the object and verified if it returns a string combination of the name and position of the player .
    
    def test_country_creation(self):
        #checking if a country is being created correctly
        #let us first check if the country_name is set properly 
        country_=Country('Somalia', [Player('Hale', '21', 'Somalia', '100', 'GK'), Player('Amen', '20', 'Somalia', '92', 'GK')])
        #let us check if the players list is assigned to the player_list attribute
        self.assertEqual(country_.country_name, 'Somalia')
        x={repr(i) for i in country_.player_list}
        self.assertSetEqual(x, {'Hale, GK', 'Amen, GK'})

    def test_get_best_player_and_number_of_world_classes(self):
        all_countries=soccer_player.convert_csv_file_to_objects()
        for i in all_countries:
            if i.country_name=='Argentina':
                result1=i 
            if i.country_name=='Equatorial Guinea':
                result2=i
        #we will prepare 3 test cases
        #the first one will test how the function will deal with a team that has no players
        #the second case will check for a team with 2 players that have equal overalls above 80
        #the third case will check for a team with a number of players that have a lot of overalls greater than 80
        #testing for a country with a large number of players of overall score greater than 80 players
        
        
        #test case 1
        #testing for a country with no player that is above 80 
        Guinea_=result2.get_best_player_and_number_of_world_classes()
        self.assertEqual(Guinea_, 'No world class')

        #test case 2
        #checking for a team with 2 players that have equal overalls above 80
        country_=Country('Somalia', [Player('Hale', '21', 'Somalia', '92', 'GK'), Player('Amen', '20', 'Somalia', '92', 'GK')])
        case_2=country_.get_best_player_and_number_of_world_classes()
        self.assertEqual(case_2, ('Hale', 2))
        
        #test case 3
        #checking for a team with a number of players that have a lot of overalls greater than 80
        Argentina_=result1.get_best_player_and_number_of_world_classes()
        self.assertEqual(Argentina_, ('L. Messi', 33))
    
    def test_get_best_player_for_position(self):
        #I chose equatorial guinea as my team
        all_countries=soccer_player.convert_csv_file_to_objects()
        for i in all_countries:
            if i.country_name=='Equatorial Guinea':
                result=i
                break
        #I decided to consider 4 cases 
        #The first case where the number of players satisfying the condition is equal to the no of players inputted
        #The second case where the number of players satisfying the condition is less than the no of players inputted
        #The third where there are no players satisfying the conditon
        #The 4th case where there are more players satisfying the condition than the input size and where 2 players have have the same overall rating but there is no enough space
        #I checked using the name and positon of the players
        
        #first case
        result1=result.get_best_player_for_position('MF', 3)
        result1={repr(i) for i in result1}
        self.assertSetEqual(result1,{'Pedro Obiang, LCM','Iban Salvador, CAM', 'José Machín, RCM'} )

        #second case
        result1=result.get_best_player_for_position('DF', 3)
        result1={repr(i) for i in result1}
        self.assertSetEqual(result1,{'Akapo, LB'} )

        #third case
        result1=result.get_best_player_for_position('FW', 3)
        self.assertListEqual(result1,[] )

        #fourth case
        
        country_=Country('Somalia', [Player('Hale', '21', 'Somalia', '92', 'GK'), Player('Amen', '20', 'Somalia', '92', 'GK')])
        case4=country_.get_best_player_for_position('GK', 1)
        case4={repr(i) for i in case4}
        self.assertSetEqual(case4, {'Amen, GK'})


    def test_get_best_players_for_each_position(self):
         #I will test it using 2 test cases
         #The first one checks if it works for a country with all overalls different
         #The second one checks for a country with 2 players of the highest overall are compared based on the age 
         
         #case 1
         country_1=Country('Somalia', [Player('Hale', '21', 'Somalia', '92', 'GK'), 
                                    Player('Amen', '20', 'Somalia', '93', 'GK'),
                                    Player('Murad', '19', 'Somalia', '94', 'LB'),
                                    Player('Abbas', '19', 'Somalia', '84', 'LB'),
                                    Player('Kaleb', '20', 'Somalia', '95', 'LM'),
                                    Player('Dior', '19', 'Somalia', '83', 'LM'),
                                    Player('Mele', '20', 'Somalia', '96', 'LW'),
                                    Player('Biruk', '20', 'Somalia', '86', 'LW')
         ])
         case_1=country_1.get_best_players_for_each_position()
         case_1={repr(i) for i in case_1}
         self.assertSetEqual(case_1,{'Amen, GK', 'Murad, LB', 'Kaleb, LM', 'Mele, LW'})

         #case 2
         country_2=Country('Somalia', [Player('Hale', '21', 'Somalia', '92', 'GK'), 
                                    Player('Amen', '20', 'Somalia', '92', 'GK'),
                                    Player('Murad', '19', 'Somalia', '92', 'LB'),
                                    Player('Kaleb', '20', 'Somalia', '92', 'LM'),
                                    Player('Mele', '20', 'Somalia', '92', 'LW')
         ])
         case_2=country_2.get_best_players_for_each_position()
         case_2={repr(i) for i in case_2}
         self.assertSetEqual(case_2,{'Amen, GK', 'Murad, LB', 'Kaleb, LM', 'Mele, LW'})
         
    
    def test_get_best_formation(self):
        # I am gonna prepare 4 test cases
        # 1st)I am gonna check the best formation for a team with complete players: 
        # 2nd)I am gonna check for a formation that doesn't fit defender-midfielder-attacker formation
        # 3rd)I am gonna check with more than 11 players formation
        # 4th)I am gonna check for a team that doesn't have enough players
        
        all_countries=soccer_player.convert_csv_file_to_objects()
        for i in all_countries:
            if i.country_name=='Argentina':
                result1=i 
            if i.country_name=='Equatorial Guinea':
                result2=i
        #test case #1
        #checking for a team with complete players  
        case_1=result1.get_best_formation('4-4-2')
        case_1={repr(i) for i in case_1}
         #I checked using the name and position of the players
        self.assertSetEqual(case_1,{'G. Rulli, GK', 'N. Tagliafico, LB', 'F. Fazio, LCB', 'E. Garay, RCB', 'N. Otamendi, CB', 'F. Vázquez, LCM', 'J. Pastore, CAM', 'E. Banega, CDM', 'A. Di María, RM', 'P. Dybala, LF', 'L. Messi, RF'})
              
        #test case #2
        #checking for a formation that doesn't fit defender-midfielder-attacker formation
        case_2=result1.get_best_formation('4-3-2-1')
        self.assertEqual(case_2, "Wrong formation")

        #test case #3
        #checking for a formation that has more than 11 players
        case_3=result1.get_best_formation('4-4-3')
        self.assertEqual(case_3, "Wrong formation")

        #test case#4
        #checking for a team that doesn't have enough players that fit a particular formation 
        case_4=result2.get_best_formation('4-3-3')
        self.assertEqual(case_4, "Not enough players")
        
        
    
# if __name__=='__main__':
#      unittest.main()
