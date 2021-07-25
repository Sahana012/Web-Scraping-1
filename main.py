from bs4 import BeautifulSoup
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)

soup = BeautifulSoup(page.text,'html.parser')

star_table = soup.find('table')

star_list= []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(star_list)):
    Star_names.append(star_list[i][1])
    Distance.append(star_list[i][3])
    Mass.append(star_list[i][5])
    Radius.append(star_list[i][6])
    
df = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df)

df.to_csv('bright_stars.csv')
