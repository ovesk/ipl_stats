# IPL Stats

This project is buid in Python Django to serve some statstical data for IPL (on fixed data in DB).
In IPL Stats the app stats contains all the statistical data fetching logics.

### Data that can be fetched from this app are:
1. Top 4 teams in terms of wins
2. Which team won the most number of tosses in the season
3. Which player won the maximum number of Player of the Match awards in the whole season
4. Which team won max matches in the whole season
5. Which location has the most number of wins for the top team
6. Which % of teams decided to bat when they won the toss.
7. Which location hosted most number of matches 
8. Which team won by the highest margin of runs for the season
9. Which team won by the highest number of wickets for the season
10. How many times has a team won the toss and the match.
11. Which Batsman gave away the most number of runs in a match for the selected season
12. Most number of catches by a fielder in a match for the selected season.

## How to use on local.
1. Pull this repository on local
2. navigate to the repository on command line.
3. Connect the desired data base in the settings.py
4. pip install requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. open a web browser and open this address http://localhost:8000/
9. Enter the desired year to check data for the given year.
