import csv
# all_players=[]
# with open('data.csv', 'r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         all_players+=[row]
# print('hale')

# my_list=[]
# for player in all_players:
#     country='Spain'
#     if player[2]==country:
#         my_list.append(player[0])
# print(my_list)

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
                if player.overall >= best_player_overall:
                    best_player = player.name
                    best_player_overall = player.overall

        return best_player, cnt

    def get_best_player_for_position(self, position, number):
        answer = [None] * number

        for player in self.player_list:
            if player.position in POSITIONS[position]:
                for i in range(len(answer)):
                    if answer[i] is None or player > answer[i]:
                        answer[i] = player

        return answer

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
        result = []

        for i, pos in enumerate(POSITIONS.keys()):
            result += self.get_best_player_for_position(pos, int(target[i]))

        return result


class Player:
    def __init__(self, name, age, nationality, overall, position):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.overall = overall
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
        return str(self)


def convert_csv_file_to_objects():
    final_players = []

    with open('data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            final_players.append(row)

    country_objects = []
    country2players = dict()
    for player in final_players:
        country2players[player[2]] = []
        country2players[player[2]].append(Player(player[0], player[1], player[2], player[3], player[4]))

    for c, p in country2players.items():
        new_country = Country(c, p)
        country_objects.append(new_country)

    return country_objects


def get_country_object_by_country_name(objects, country_name):
    for country in objects:
        if country.country_name == country_name:
            return country

    return 'No such country'


x = convert_csv_file_to_objects()
for i in x:
    if i.country_name == 'Argentina':
        result = i  # Argentina Team players
        break

for i in range(len(result.player_list)):
    print(result.player_list[i].name)
    print(result.player_list[i].overall)
    print(result.player_list[i].age)
    print(result.player_list[i].position)
print(result.get_best_player_for_position('FW', 2))

