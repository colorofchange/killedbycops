import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'killedbycops.settings'

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command

sched = BlockingScheduler()

@sched.scheduled_job('cron', id='post_one_tweet', hour='*', minute='0')
def timed_job():
    call_command('post_one_tweet')

print "starting scheduler"
sched.start()
