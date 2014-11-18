Nebraska choroplethinator
======

<img src="http://i.imgur.com/ao8NFCi.png?1" />

A Python script adapted from <a href="http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/">this example</a> that shades SVG maps of Nebraska counties, in batches, based on csv data. The data samples here came from <a href="http://electionresults.sos.ne.gov/ResultsExport.aspx">Excel files</a> of results from Nebraska's 2014 general election.

Assumptions:
<ul>
<li>You're rocking a Windows machine (hello, World-Herald peeps!).</li>
<li>The first column in each .csv is the county name.</li>
<li>For each column in each file, you've added a descriptive name and associated colors to the list that starts around line 13 (see the note). The name matches (or is included in) the file name.</li>
<li>You have <a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a> installed. Optional: <a href="https://inkscape.org/en/">Inkscape</a>, if you want to use the <a href="https://github.com/cjwinchester/ne-county-choropleth/blob/master/svg2png.bat">management script</a> to spit out PNGs.</li>
</ul>