import csv
from bs4 import BeautifulSoup

"""

Data sample is a csv carved out of this .xls file: http://electionresults.sos.ne.gov/ResultsExport.aspx?rid=702&pty=&name=For%20Governor%20and%20Lt.%20Governor&cat=CTY

Method adapted from: http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

"""

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