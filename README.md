# styleru_py_week1
This is result of my work with TMDB api:  
All of these scripts requires Python 3.x.  
Each program could work separate, but 3rd and 4th need DataBase from the second task to work.  
Also there is full Eng interface.  


***
# 1. Hello_api_TMDB #
#### This is the first task, 
I made function for searching film budget by it's number in TMDB.  
You need to enter your api_key_v3, wich you could get [here](https://www.themoviedb.org/).  
Then program print budget of film №215 in TMDB.  
#### example of code process:
  ***Enter your api key v3***  
  *64be4144d51bbaee6234f2w82bb*  
  ***4000000***  
  ***Process finished with exit code 0***  
  
***
# 2. My_own_DB #
#### Second task,
I made program to download info about 1000 films from TMDB.  
You could find this info in file MyFilmBD.json after run.  
It also requires api_key_v3.  
#### example of code process:  
  ***Enter your api key v3***  
  *64be4144d51bbaee6234f2w82bb*  
  **(here would be percents of code process)**  
  ***Process finished with exit code 0***  
  > Remember, that you must delete this in couple of days, because TMDB don't allow to save their data      
  
***
# 3. Search_in_DataBase #
#### Third task,
This program search for film in DataBase from second task.  
You must enter path to DataBase, and then program will search for your film and print similar results.  
#### example of code process:  
  ***Enter path to DataBase:***  
  *MyFilmBD.json*  
  ***Enter film to search for:***  
  *Saw*  
  ***Saw***  
  ***Saw II***  
  ***Saw III***  
  ***Saw IV***  
  ***Process finished with exit code 0***  
  ***
# 4. Search_for_similar_films #
#### Fourth task,
This program will try to find similar to your entered film.  
You must print **correct** title to find smth.  
Also you must enter path to your DataBase.  
#### example of code process:  
  ***Enter path to DataBase:***  
  *MyFilmBD.json*  
  ***Enter film to search for:***  
  *Saw*    
  ***Saw II***  
  ***Saw III***  
  ***Saw IV***  
  ***Harold and Maude***  
  ***Il buono, il brutto, il cattivo***  
  ***Reservoir Dogs***  
  ***Strangers on a Train***  
  ***The Day the Earth Stood Still***   
  ***Process finished with exit code 0***  
