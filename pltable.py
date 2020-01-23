from bs4 import BeautifulSoup
import pandas as pd
import requests
teams = []
points = []
played = []
place = []
page = requests.get("https://www.premierleague.com/tables")
soup = BeautifulSoup(page.content ,"html.parser")
table = soup.find_all(class_="table wrapper col-12")
container = soup.find_all(class_="long")
cnt = soup.find_all(class_="points")
for i in range(0,20):
    teams.append(container[i].get_text())
    points.append(cnt[i+1].get_text())
    place.append(i+1)
xcel = pd.DataFrame({"place" : place , "Teams" : teams ,"points" : points})
xcel.to_csv("pltable.csv")
print(xcel)

