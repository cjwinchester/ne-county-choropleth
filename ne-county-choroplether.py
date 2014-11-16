import csv
from bs4 import BeautifulSoup

counties = {}
reader = csv.reader(open('governor_county_cleaned.csv'), delimiter=",")

for row in reader:
    county = row[0].replace(" ","-").lower()
    hassebrook = row[1]
    elworth = row[2]
    ricketts = row[3]
    winner = max(int(hassebrook), int(elworth), int(ricketts))
    if winner == int(hassebrook):
        win_color = "#6baed6"
    elif winner == int(ricketts):
        win_color = "#fb6a4a"
    elif winner == int(elworth):
        win_color = "#c09853"
    counties[county] = win_color

svg = open('ne-counties.svg', 'rb').read()

path_style = "color:#aaa; stroke:#000; stroke-width:0.5; stroke-linecap:butt; stroke-linejoin:miter; stroke-miterlimit:4; fill:"

soup = BeautifulSoup(svg, "html.parser")

paths = soup.findAll('path')

for p in paths:
    color = counties[p['id']]
    p['style'] = path_style + color
    
print soup.prettify()

# usage: python ne-county-choroplether.py > governor_results.svg