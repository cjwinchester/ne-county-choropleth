import csv
from bs4 import BeautifulSoup

counties = {}
reader = csv.reader(open('governor_county_cleaned.csv'), delimiter=",")

colors = ['#6baed6', '#c09853', '#fb6a4a']

for row in reader:
    county = row[0].replace(" ","-").lower()
    nums = []
    for thing in row[1:]:
        nums.append(int(thing))
    winner = max(nums)
    position = nums.index(winner)
    win_color = colors[position]
    counties[county] = win_color
    
svg = open('ne-counties.svg', 'rb').read()

path_style = "color:#aaa; stroke:#fff; stroke-width:1; stroke-linecap:butt; stroke-linejoin:miter; stroke-miterlimit:4; fill:"

soup = BeautifulSoup(svg, "html.parser")

paths = soup.findAll('path')

for p in paths:
    color = counties[p['id']]
    p['style'] = path_style + color
    
print soup.prettify()