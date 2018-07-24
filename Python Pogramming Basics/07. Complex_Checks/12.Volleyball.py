import math
year = input()
holidays = int(input())
weekends_home = int(input())

Sofia_Games = (48 - weekends_home) * 3 / 4
home_games = weekends_home
Sofia_holiday_games = holidays * 2 / 3
total_games = Sofia_Games + home_games + Sofia_holiday_games
if year == "leap":
    total_games = total_games * 1.15

print(math.floor(total_games))
