from celery import Celery
from django.core.mail import send_mail

app = Celery('celery_tasks.tasks', broker='redis://192.168.12.189:6379/3')

'''给celery看  运行django里面的信息用'''
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

#启动命令
#celery -A celery_tasks.tasks worker -l info

@app.task
def task_send_mail(subject, message, sender, receiver, html_message):
    print('发邮件begin....')
    import time
    time.sleep(10)
    send_mail(subject, message, sender, receiver, html_message=html_message)
    print('发邮件end....')