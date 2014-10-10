import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

def tweet_hourly():
    print "tweet_hourly"
    print subprocess.call(["python","manage.py","post_one_tweet"])
    print "done"

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    print "setup APScheduler.Blocking"
    scheduler.add_job(tweet_hourly, 'cron', id='tweet_hourly', hour='*', minute='0')

    try:
        print "starting... control-C to quit"
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print "scheduler quit"
        pass