from bs4 import BeautifulSoup
import pandas as pd
import requests
teams = []
points = []
played = []
place = []
goals_for = []
goals_against = []
page = requests.get("https://www.premierleague.com/tables")
soup = BeautifulSoup(page.content ,"html.parser")
table = soup.find_all(class_="table wrapper col-12")
container = soup.find_all(class_="long")
cnt = soup.find_all(class_="points")
goals = soup.find_all("td",class_ ="hideSmall")
for i in range(40):
    if i%2 == 0:
        goals_for.append(goals[i].get_text())
    else:
        goals_against.append(goals[i].get_text())
for i in range(0,20):
    teams.append(container[i].get_text())
    points.append(cnt[i+1].get_text())
    place.append(i+1)
xcel = pd.DataFrame({"place" : place , "Teams" : teams ,  "Goals Against" : goals_against, "Goals For" : goals_for,"points" : points})
xcel.to_csv("pltable.csv")
