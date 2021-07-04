#IPL Stats

This project is buid in Python Django to serve some statstical data for IPL (on fixed data in DB).
In IPL Stats the app stats contains all the statistical data fetching logics.

Data that can be fetched from this app are.
    • Top 4 teams in terms of wins
    • Which team won the most number of tosses in the season
    • Which player won the maximum number of Player of the Match awards in the whole season
    • Which team won max matches in the whole season
    • Which location has the most number of wins for the top team
    • Which % of teams decided to bat when they won the toss.
    • Which location hosted most number of matches 
    • Which team won by the highest margin of runs for the season
    • Which team won by the highest number of wickets for the season
    • How many times has a team won the toss and the match.
    • Which Batsman gave away the most number of runs in a match for the selected season
    • Most number of catches by a fielder in a match for the selected season.

##How to use on local.
1. Pull this repository on local
2. navigate to the repository on command line.
3. Connect the desired data base in the settings.py
4. pip install requirements.txt
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver
8. open a web browser and open this address http://localhost:8000/
9. Enter the desired year to check data for the given year.
