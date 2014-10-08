killedbycops
============

A Twitter memorial to Americans killed by cops.
All data provided by FatalEncounters.org
Images (c) 2014 ColorOfChange.org

## Setup
Create a twitter app for the @killedbycops user:
https://apps.twitter.com

Add keys to the environment:
> heroku config:add TWITTER_CONSUMER_KEY=
> heroku config:add TWITTER_CONSUMER_SECRET=

Generate token and add to the environment:
> heroku config:add TWITTER_TOKEN_KEY=
> heroku config:add TWITTER_TOKEN_SECRET=

Load FatalEncounters data:
> python manage.py update_fatal_encounters [--pull_from_web]

Generate tweets:
> python manage.py generate_tweets --attach_image [--overwrite_existing]

Post one tweet an hour, using cron or Heroku delayed jobs:
> python manage.py post_one_tweet [--geocode]
