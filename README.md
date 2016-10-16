# Hype surrounding the release of „World of Warcraft – Legion“ at 08/30/2016 
In what countries the release of "World of Warcraft - Legion" will be most hyped via twitter 
and what languages are the most tweeted ones? 
An analysis about fetching tweets to #legion #worldofwarcarf and #warcraft and visualizing them with python.


Features

	- Twitter-Crawler to fetch tweets via client or timeline.
	- creating world map and drawing geo-tags of tweets in different colors depending on its language with 
	  matplotlib and basemap.
	- creating and drawing two donut plots with bokeh to show the statistc of the different languages in combination 
	  with langdetec and twitter language detection.
	- creating and drawing one bar plot with bokeh to show a statistic from tweets and the country of it's user.

These instructions will get you a copy of the project up and running on your local machine.

Prerequisities

What things you need to install the software and how to install them

You need Python 2.7 get it here:
https://www.python.org/download/releases/2.7/
and you need a twitter account with access tokens to use the crawler for tweets 

A step by step series of instructions on how to get the code running

Get an API Access Key/Token for twitter.

	- for an english guide check the official twitter guide via
	  <a href="https://dev.twitter.com/oauth/overview/application-owner-access-tokens/">How to generate Twitter Keys</a>
	- for a german guide check my dokumentation PDF (included)
	- insert your generated keys/tokens in the twitter_keys.py
	
Install Python 2.7 and get the following Libs via pip install or manual installation

	• tweepy
	• re
	• collections
	• unicodecsv
	• nltk
	• bokeh
	• matplotlib
	• mpl_toolkits.basemap
	• os
	• langdetect
	
Run the main.py to draw the plots based on the results.csv

Versioning

	- Distributed revision control system Git



Authors

- <strong>Thorsten Brückner</strong> - <a href="https://github.com/Geemania">Geemania</a>
