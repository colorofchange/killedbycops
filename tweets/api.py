import os, sys
from retrying import retry

from geopy.geocoders import GeoNames
import tweepy

if not os.environ.has_key('TWITTER_CONSUMER_KEY'):
    print "no TWITTER_CONSUMER_KEY"
    sys.exit(-1)
if not os.environ.has_key('TWITTER_CONSUMER_SECRET'):
    print "no TWITTER_CONSUMER_SECRET"
    sys.exit(-1)

twitter_auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_KEY'),
                                   os.environ.get('TWITTER_CONSUMER_SECRET'))

if not (os.environ.has_key('TWITTER_TOKEN_KEY') and os.environ.has_key('TWITTER_TOKEN_SECRET')):
    import webbrowser
    webbrowser.open_new(twitter_auth.get_authorization_url())
    verifier = raw_input('Verifier:')
    twitter_auth.get_access_token(verifier)
else:
    twitter_auth.set_access_token(os.environ.get('TWITTER_TOKEN_KEY'),
                                  os.environ.get('TWITTER_TOKEN_SECRET'))

twitter_api = tweepy.API(twitter_auth)

def twitter_geocode(city, state):

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def geocode(string):
      geolocator = GeoNames(username='jlevinger')
      return geolocator.geocode(string)
      
    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def reverse_geocode(lat, lon):
      try:
        return twitter_api.reverse_geocode(lat, lon, granularity='city')
      except tweepy.error.TweepError:
        return False

    location = geocode("%s, %s" % (city, state))
    twitter_location = reverse_geocode(location.latitude, location.longitude)
    return twitter_location.ids()[0]
