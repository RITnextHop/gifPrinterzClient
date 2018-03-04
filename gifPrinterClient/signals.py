from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Upload
import ftplib
from IPython import embed

@receiver(post_save, sender=Upload)
def print_gif(sender, instance, **kwargs):
    session = ftplib.FTP('192.168.2.234', 'anonymous', 'password')
    #session.login()
    gif_path = 'media/'+str(instance.gif)
    gif_file = open(gif_path,'rb')
    cmd = 'STOR pub/'+str(instance.gif).split('/')[-1]
    #embed()
    session.storbinary(cmd, gif_file)
    gif_file.close()
    session.quit()
