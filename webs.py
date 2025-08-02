 #import section
import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get('https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=540a03b3-e792-42fc-bda8-1aadb7076cf9')

soup = BeautifulSoup(response.text, 'html.parser')

# Extracting the table from the HTML
names=soup.find_all('div')
name=[]
for i in names[12]:
    d=i.text
    name.append(d)
print(name)
# Extracting the data into a DataFrame