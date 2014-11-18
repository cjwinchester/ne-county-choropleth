import glob
import csv
from bs4 import BeautifulSoup

files = glob.glob('*.csv')

"""

Add colors for each column in each csv to the list below. Example: In the race for Nebraska governor in 2014, the Secretary of State results ordered the candidates with Hassebrook (D) first, then Elworth (L), then Ricketts (R). So the color order in the associated list is '#6baed6' (blue), '#c09853' (gold), '#fb6a4a' (red). The descriptive name in the first position needs to either match or be included in the associated file name. For instance, 'governor' is included in the file name 'governor_county_cleaned.csv'.

"""

colors = [
['governor', ['#6baed6', '#c09853', '#fb6a4a']],
['senate', ['#fb6a4a', '#6baed6', '#00c199', '#c994c7']]
]

for file in files:
    counties = {}
    reader = csv.reader(open(file), delimiter=",")
    for row in reader:
        county = row[0].replace(" ","-").lower()
        nums = []
        for thing in row[1:]:
            nums.append(int(thing))
        winner = max(nums)
        for color in colors:
            if color[0] in file:
                win_color = color[1][nums.index(winner)]
                counties[county] = win_color
        
    svg = open('ne-counties.svg', 'rb').read()
    output = open(str(file).replace('.csv','') + '_output.svg', 'wb')
    
    path_style = "color:#aaa; stroke:#fff; stroke-width:1; stroke-linecap:butt; stroke-linejoin:miter; stroke-miterlimit:4; fill:"

    soup = BeautifulSoup(svg, "html.parser")

    paths = soup.findAll('path')

    for p in paths:
        color = counties[p['id']]
        p['style'] = path_style + color
        
    output.write(soup.prettify())
    output.flush()
    output.close()