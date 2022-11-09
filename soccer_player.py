import csv

POSITIONS = {'GK': ['GK'],
             'DF': ['LB', 'LCB', 'CB', 'RCB', 'RB', 'LWB', 'RWB'],
             'MF': ['LDM', 'CDM', 'RDM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LAM', 'CAM', 'RAM'],
             'FW': ['LW', 'RW', 'LS', 'ST', 'RS', 'LF', 'CF', 'RF']}


class Country:
    def __init__(self, country_name, player_list):
        self.country_name = country_name
        self.player_list = player_list

    def get_best_player_and_number_of_world_classes(self):
        cnt = 0
        best_player = None
        best_player_overall = 0
        for player in self.player_list:
            if player.overall >= 80:
                cnt += 1
                #I removed the equal to sign on the below if condition
                #It was returning the last element in the list if there are 2 players with equal overalls
                if player.overall > best_player_overall:
                    best_player = player.name
                    best_player_overall = player.overall
        #checking if there are no world class players
        #original source code didn't do this 
        if best_player==None:
            return 'No world class'
        return best_player, cnt

    def get_best_player_for_position(self, position, number):
        answer = [None] * number

        for player in self.player_list:
            if player.position in POSITIONS[position]:
                # it wasn't returning properly,
                # a player with the largest overall will replace all the other players and the list will contain only one element
                # it was rewriting on elements even when there was available position
                # I fixed it so that it would rewrite only when there is no none left and also I sorted the list before checking players to rewrite
                # so if there is any player to rewrite we will rewrite only the first player
    
                for i in range(len(answer)):
                    if answer[i] is None: 
                        answer[i] = player
                        break
                    elif None not in answer:
                        answer.sort()
                        if answer[i]<player:
                            answer[i]=player
                            break
        #Resizing the list
        if None in answer:
            x=answer.index(None)
            answer=answer[:x]
        return answer
    # def get_best_player_for_position(self, position, number):
    #     answer = [None] * number

    #     for player in self.player_list:
    #         if player.position in POSITIONS[position]:
    #             for i in range(len(answer)):
    #                 if answer[i] is None or player > answer[i]:
    #                     answer[i] = player

    #     return answer

    def get_best_players_for_each_position(self):
        bests = [None, None, None, None]

        for player in self.player_list:
            for i, position in enumerate(POSITIONS.keys()):
                if player.position in POSITIONS[position]:
                    if bests[i] is None or player > bests[i]:
                        bests[i] = player

        return bests

    def get_best_formation(self, formation):
        target = ['1']
        target += formation.split('-')
        #I made it check if the formation is valid and if the number of players is enough to fit
        sum=0
        for i in target:
            sum+=int(i)
        if(sum!=11 or len(target)!=4):
            return "Wrong formation"
        
        result = []
        for i, pos in enumerate(POSITIONS.keys()):
            result += self.get_best_player_for_position(pos, int(target[i]))

        #checking if their aren't enough players for the positon 
        if len(result)<11:
            return "Not enough players"
       
        return result


class Player:
    # I fixed it so that the age and overall rating are
    def __init__(self, name, age, nationality, overall, position):
        self.name = name
        self.age = int(age)
        self.nationality = nationality
        self.overall = int(overall)
        self.position = position

    def __gt__(self, other):
        if self.overall > other.overall:
            return True
        if self.overall < other.overall:
            return False
        if self.age < other.age:
            return True
        return False

    def __str__(self):
        return self.name

    def __repr__(self):
        # this is just returing the players name so we need to fix it
        # return str(self):- it is just doing what the above function does
        # instead we need to return the players name and position as a string
        return self.name+", "+self.position


def convert_csv_file_to_objects():
    final_players = []

    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            final_players.append(row)

    country_objects = []
    country2players = dict()
    for player in final_players:
        # The code doesn't create the player_list properly and exhaustively.
        # It just adds only assigns a single player to a single country.
        # It should instead return a list of the players of a particular country
        if not (player[2] in country2players.keys()):
            country2players[player[2]] = []
        country2players[player[2]].append(
            Player(player[0], player[1], player[2], player[3], player[4]))

    for c, p in country2players.items():
        new_country = Country(c, p)
        country_objects.append(new_country)
    return country_objects


def get_country_object_by_country_name(objects, country_name):
    for country in objects:
        if country.country_name == country_name:
            return country

    return 'No such country'


# player_3=Player("Halleluyah", 21, "Ethiopia", 100, 'LW')
# print(repr(player_3))
x = convert_csv_file_to_objects()
for i in x:
    if i.country_name == 'Brazil':
        result = i  
print(result.get_best_formation('3-4-3'))
# for i in range(len(result.player_list)):
#     print((result.player_list[i].name, result.player_list[i].age, result.player_list[i].nationality, result.player_list[i].overall,result.player_list[i].position))
#print(result.get_best_player_for_position('FW', 10))
# print(result.get_best_formation('4-4-2'))
# print(get_country_object_by_country_name(x, 'Somalia'))
# # counter=0
# # for i in x:
# #     if(len(i.player_list)==5):
# #         print(i.country_name)
# #         print(counter)
# #     counter+=1

# for i in range(len(x[0].player_list)):
#     print(x[0].player_list[i].name)
#     print(x[0].player_list[i].overall)
