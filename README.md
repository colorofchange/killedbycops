killedbycops
============

A Twitter memorial to Americans killed by cops. All data provided by FatalEncounters.org
Images (c) 2014 ColorOfChange.org

## Setup
Create a twitter app for the @killedbycops user:
https://apps.twitter.com

Add keys to the environment:
TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET

Generate token and add to the environment:
TWITTER_TOKEN_KEY, TWITTER_TOKEN_SECRET

Generate tweets:
> python manage.py generate_tweets --attach_image [--overwrite_existing]

Post one tweet an hour, using cron or Heroku delayed jobs:
> python manage.py post_one_tweet [--geocode]
