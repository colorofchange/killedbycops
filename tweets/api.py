import tweepy, os

if not os.environ.has_key('TWITTER_CONSUMER_KEY'):
    print "no consumer key"
if not os.environ.has_key('TWITTER_CONSUMER_SECRET'):
    print "no consumer secret"

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