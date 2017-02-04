import subprocess
import datetime


class Task():
    ''' Task object stores details about the task to be scheduled or reminded of
        
        Parameters
        ----------

        name : Task keywords or short description
        date : 
        time :

    '''

    def __init__(self, name='Reminder', time='default', date='default'):
       
        now = datetime.datetime.now()

        self.name = name

        if (date == 'default'):
           self.date = str(now.day)+ '/'+ str(now.month) + '/' + str(now.year) 
        else:
            self.date = date

        if (time == 'default'):
            self.time =str(now.hour) +':'+str(now.minute + 1)
        else:
            self.time = time

    def schedule(self):
        ''' Schedules the task in crontab '''

        hour,minute = self.time.split(':')

        subprocess.call(['./schedule.sh',self.name, hour, minute])

    def notify_Desktop(self):     
        ''' Sends a desktop notfication using notify-send '''

        subprocess.call(['./notify.sh',self.name])
