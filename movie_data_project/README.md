## Movie Data Project: Web Scraping to SQLite ETL
* This project extracts highly-ranked film data from a web archive, transforms it, and loads it into a local SQLite database and a CSV file. It also provides a simple terminal interface to query the loaded data.

## Project Description
* This project automates collecting, cleaning, and storing film data from a web page. It extracts film details (Rank, Title, Year), saves them to a CSV, and loads them into a SQLite database. A command-line interface lets users query the data by release year.

## Project Structure
```
movie_data_project/
├── webscraping_movies.py
├── main_orchestration.py
├── Movies.db (generated after running ETL)
├── top_50_films.csv (generated after running ETL)
└── README.md
``` 

## How It Works
- webscraping_movies.py: Handles the ETL process.

- Extracts film data from a web archive using requests and BeautifulSoup.
- Transforms the data into a Pandas DataFrame, cleaning and structuring it.
- Loads the transformed data into top_50_films.csv and the Movies.db SQLite database (Top50Movies table).
- main_orchestration.py: The main control script.

* Orchestrates the ETL process by calling functions from webscraping_movies.py.
Provides a terminal menu to either run the ETL or query films from Movies.db by release year.

## How to Run
* Setup: Create a directory named movie_data_project and place both webscraping_movies.py and main_orchestration.py inside it.
* Install Dependencies:
Bash
pip install requests beautifulsoup4 pandas
Run: From your terminal, navigate to movie_data_project and execute:
Bash
python main_orchestration.py
Interact: Follow the menu prompts. First, run the ETL (Option 1) to populate the database, then you can query films (Option 2).


```
--- Film Database Application Menu ---
1. Run ETL (Extract, Transform, Load) process
2. Query films released after a specific year
3. Exit
--------------------------------------
Enter your choice (1, 2, or 3): 
``` 
* if choice 1:
```
Running ETL process...
Starting ETL process from URL: https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films
Data successfully saved to top_50_films.csv
Data successfully loaded into Movies.db in table 'Top50Movies'.
ETL process completed successfully. Database and CSV updated.
```
* if choice 2:
```
Enter the year (e.g., 2000) or 'back' to return to main menu: 2001

--- Films released after 2001 ---
Average Rank                                  Film Year
          17                              Parasite 2019
          23                     Avengers: Endgame 2019
          34     Spider-Man: Into the Spider-verse 2018
          37                       The Dark Knight 2008
          41                    Mad Max: Fury Road 2015
          42                             Inception 2010
          43 Lord of the Rings: Return of the King 2003
          49     Lord of the Rings: The Two Towers 2002
-----------------------------------

```
* choice 3 (quiting)
```
Exiting the program. Goodbye!
``` 
