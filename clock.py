import subprocess
from retrying import retry

from apscheduler.schedulers.blocking import BlockingScheduler

def next_tweet():
    print "post next tweet"

    #track number of attempts, for skip argument
    attempt = [-1,] #must be a list to be mutable by inner function, init at -1 bc exception thrown on return

    def retval_is_nonzero(retval):
        had_error = retval is not 0
        if had_error:
            print "error, subprocess returned",retval
        return had_error

    # retry after 20 seconds, up to a maximum of 3 times
    @retry(retry_on_result=retval_is_nonzero, stop_max_attempt_number=3, wait_fixed=20000)
    def call_subprocess():
        attempt[0] = attempt[0]+1
        print "attempt",attempt
        call = ["python","manage.py","post_next_tweet","--skip=%d" % attempt[0]]
        print "calling > %s" % ' '.join(call)
        return subprocess.call(call)

    call_subprocess()
    print "success"

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    print "setup APScheduler.Blocking"
    scheduler.add_job(next_tweet, 'cron', id='next_tweet', hour='*', minute='0')

    try:
        print "starting... control-C to quit"
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print "scheduler quit"
        pass
