import subprocess
from retrying import retry

from apscheduler.schedulers.blocking import BlockingScheduler

def random_tweet():
    def retval_is_nonzero(retval):
        had_error = retval is not 0
        if had_error:
            print "error, subprocess returned",retval
        return had_error

    # retry after 20 seconds, up to a maximum of 3 times
    @retry(retry_on_result=retval_is_nonzero, stop_max_attempt_number=3, wait_fixed=20000)
    def call_subprocess():
        print "calling > python manage.py post_random_tweet"
        return subprocess.call(["python","manage.py","post_random_tweet"])

    call_subprocess()
    print "done"

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    print "setup APScheduler.Blocking"
    scheduler.add_job(random_tweet, 'cron', id='random_tweet', hour='*', minute='0')

    try:
        print "starting... control-C to quit"
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print "scheduler quit"
        pass
