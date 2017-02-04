import subprocess

class Task():
    ''' Task object stores details about the task to be scheduled or reminded of
        
        Parameters
        ----------

        name : Task keywords or short description
        date : 
        time :

    '''

    def __init__(self, name='Reminder', time='345', date='345'):

        self.name = name
        self.date = date
        self.time = time

    def schedule(self):
        ''' Schedules the task in crontab '''

        hour = self.time[:1]
        minute = self.time[2:]

        subprocess.call(['./schedule.sh',self.name, hour, minute])

    def notify_Desktop(self):     
        ''' Sends a desktop notfication using notify-send '''

        subprocess.call(['./notify.sh',self.name])
