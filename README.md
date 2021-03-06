KilledByCops
============

A visualization of Americans killed by cops: 2000-2015
* Data from FatalEncounters.org, US Census, Center for Constitutional Policing
* Images and map design &copy; 2015 ColorOfChange.org 

# Overview

This project consists of two distinct parts, a Twitter application that sends tweets to the @killedbycops accounts, and a map visualizing the included FatalEncounters data. The Twitter application can be run on Heroku, and the map can be rendered to static files to be served by GitHub pages via the _site directory.

# Data Sources

### FatalEncounters

Their data is stored in a google spreadsheet, which we have cached and cleaned up slightly at `fatalencounters/data/fatal-encounters.csv`. New unproofed data is appended after a yellow line in the spreadsheet; but since we don't get color output in the csv, you'll need to pass that name. It will default to the known value at last check, Dixon Rodriguez.
You can download a new copy with `> python manage.py update_fatal_encounters --pull_from_web`.

In the future this should be easier, as FatalEncounters moves to a new database with an API.

### US Census

Download from http://factfinder2.census.gov. Specific instructions at http://bost.ocks.org/mike/bubble-map/#finding-data

Take care with updating the US Census data to new American Community Survey years, some areas may be missing in the 2013 data.

# Visualizations

## KilledByCops Map

The map is created with D3, with the database and documents saved as JSON files. If running the server locally, you can recreate the cache file with `cd map/data; make`.

### Static Site Rendering

Render the html and static files with:
> python manage.py staticsitegen
> python manage.py collectstatic

Push the resulting directory to a gh-pages branch, and GitHub Pages will serve it for free.

### KilledByCops Twitter App

Create a twitter app for the @killedbycops user:
https://apps.twitter.com

Add keys to the environment:
> heroku config:add TWITTER_CONSUMER_KEY=  
> heroku config:add TWITTER_CONSUMER_SECRET=  

Generate token and add to the environment:
> heroku config:add TWITTER_TOKEN_KEY=  
> heroku config:add TWITTER_TOKEN_SECRET=  

Load FatalEncounters data:
> python manage.py update_fatal_encounters [--pull_from_web] [--last_proofed_row]

Generate tweets:
> python manage.py generate_tweets --attach_image [--overwrite_existing]

Post one tweet an hour, using cron or Heroku delayed jobs:
> python manage.py post_one_tweet [--geocode]
