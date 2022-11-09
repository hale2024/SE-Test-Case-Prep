<h1>Preparing Test Cases on Soccer Players Filtering Program</h1>

<h2>Explanation</h2>
<p>The input dataset will contain a list of soccer players and their information, including name, age, country, overall rating, and position. The
source code retrieves relevant information from this dataset by making use of initially defined functions. The defined functions are:</p>
<ul>
  <li><strong>get_best_player_and _number_of_world_classes:-</strong> A world class player is defined as a player with an overall rating >= 80, and the the best player is the player with the highest overall rating. It should return the name of the best player out of the world class players and the number of world class players in a given country. Best player is the player who has the highest overall score. If there’s a tie on the highest overall rating, it should return the name of the best player who appears first in the list. If there is no world class player, it should return a string, ‘No world class’.</li>
     <li><strong>get_best_players_for_position:-</strong>It should be able to return a list of the top n number of players from the country, given a position and the number of players to retrieve. The input position is the main position from the positions table. The best player(s) indicates the ones with highest ratings. If multiple players have the same overall ratings, younger players are favored. If there aren’t enough number of players for a given position to fill the list of n players, the list of players for the given position should still be returned. In this case, the length of the returned list should simply be the number of players with specified position.</li>
   <li><strong>get_best_players_for_each_position:-</strong>It should be able to get the best players for each of the 4 positions, goalkeeper, defender, midfielder, and forward, from the country. The best player(s) indicates the ones with highest ratings. If multiple players have the same overall ratings, younger players are favored.</li>
   <li><strong>get_best_formation:-</strong>It should return a list of best players, including the goalkeeper, for a given formation. The input formation is a - separated string for the number of players in the Defender-Midfielder-Attacker formation (e.g. ‘4-3-3’ for a formation of 4 defenders, 3 midfielders, and 3 attackers). If the input formation does not conform to the Defender-Midfielder-Attacker formation (e.g. ‘3-2-3-2’ formation), it should return ‘Wrong formation’. The sum of players in the formation should be 11 (e.g. ‘4-3-3’ formation has 10 field players and a goalkeeper). If the input formation does not have 11 players (e.g. ‘3-3-3’ formation has a total of 10 players, 9 field players and a goalkeeper), it should return ‘Wrong formation’. The position used in this function is the main position from the above table. If there are not enough players to fill the position, it should return a string, ‘Not enough players’.</li>
  <li><strong>__gt__:-</strong>It should compare the player against another player by using the overall rating first and then their ages. If the two players have the same overall rating, then their ages should be compared to favor the younger player.</li>
  <li><strong>__str__:-</strong>It should return the name of the player.</li>
   <li><strong>__repr__:-</strong>It should return the string of the players name, position. (e.g., ‘H. Son, LM’).</li>
   <li><strong>convert_csv_file_to_object:-</strong>This method should open a ‘data.csv’ file and return a list of country objects.</li>
   <li><strong>get_country_object_by_country_name:-</strong>It should be able to return the country object who has the same country_name class variable with the given country name from a list of country objects. If there is no such country, it should return a string ‘No such country’</li>

  
</ul>
<strong><p> The comprehensive tests I built ensure that accurate information retrieval is done when any of the above source code functions are called. I tested the source code with the python ‘unittest’ module and made the necessary fixes to the code.</p></strong>


<h2>Acknowledgment and Additional Information</h2>
 
<ul>
  <li>This assignment is done as part of KAIST Introduction of Software Engineering CS350 course.</li>
  <li>The instructions for this assignment are found inside cs350_spring2022_pr2.pdf.</li>
  <li>The original source code can be found in soccer_player_original.</li>
  <li>The input dataset can be found in data.csv</li>
  <li>The detailed description of my test cases can be found in pr2_Halleluyah_20200816.pdf.</li>
  <strong><li>My test cases can be found in test_soccer_player.py.</li></strong>
   <strong><li>The fixed source code can be found in soccer_player_original.</li></strong>
  <li>I recieved an A+ because my test cases were very well designed and well documented.</li>
</ul>
