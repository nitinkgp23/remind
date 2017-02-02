import subprocess

class Task():
    ''' Task object stores details about the task to be scheduled or reminded of
        
        Parameters
        ----------

        name : Task keywords or short description
        date : 
        time :

    '''

    def __init__(self, name='Reminder', date='345', time='345'):

        self.name = name
        self.date = date
        self.time = time

    def notify_Desktop(self):

        #subprocess.Popen(['notify-send',self.name])        
        #os.system('aplay -q ~/remind/res/notifications/Mallet.wav')
        subprocess.call(['./notify.sh',self.name])
