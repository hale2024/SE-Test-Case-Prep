<h1>Preparing Test Cases on Soccer Players Filtering Program</h1>

<h2>Explanation</h2>
<p>The input dataset will contain a list of soccer players and their information, including name, age, country, overall rating, and position. The
source code retrieves relevant information from this dataset by making use of initially defined functions. The defined functions are:</p>
<ul>
  <li><strong>get_best_player_and _number_of_world_classes:-</strong>A world class player is defined as players with an overall rating >= 80, and the the best player is the player with the highest overall rating</li>
     <li><strong>get_best_players_for_position:-</strong>It should be able to return a list of the top n number of players from the country, given a position and the number of players to retrieve.</li>
   <li><strong>get_best_players_for_each_position:-</strong>It should be able to get the best players for each of the 4 positions, goalkeeper, defender, midfielder, and forward, from the country.</li>
   <li><strong>get_best_formation:-</strong>It should return a list of best players, including the goalkeeper, for a given formation.</li>
  <li><strong>__gt__:-</strong>It should compare the player against another player by using the overall rating first and then their ages.</li>
  <li><strong>__str__:-</strong>It should return the name of the player.</li>
   <li><strong>__repr__:-</strong>It should return the string of the players name, position. (e.g., ‘H. Son, LM’).</li>
   <li><strong>convert_csv_file_to_object:-</strong>This method should open a ‘data.csv’ file and return a list of country objects.</li>
   <li><strong>get_country_object_by_country_name:-</strong>It should be able to return the country object who has the same country_name class variable with the given country name from a list of country objects. If there is no such country, it should return a string ‘No such country’</li>

  
</ul>
<p> The comprehensive tests I built will ensure that accurate information retrieval is done when the source code functions are called.</p>


<h2>Acknowledgment and Additional Information</h2>
 
<ul>
  <li>This assignment is done as part of KAIST Introduction of Software Engineering CS350 course.</li>
  <li>The instructions for this assignment are found inside cs350_spring2022_pr2.pdf.</li>
  <li>The source code can be found in soccer_player_original.</li>
  <li>The input dataset can be found in data.xls</li>
  <li>The detailed description of my test cases can be found in pr2_Halleluyah_20200816.pdf.</li>
  <li>My test cases can be found in test_soccer_player.py.</li>
  <li>I recieved an A+ because my test cases were very well designed and well documented.</li>
</ul>
