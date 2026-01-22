from django.core.mail import send_mail
from django.utils import timezone
from .models import Reminder

def send_reminders():
    now = timezone.localtime()
    reminders = Reminder.objects.filter(
        remind_date=now.date(),
        remind_time__hour=now.hour,
        remind_time__minute=now.minute,
        sent=False
    )

    for r in reminders:
        send_mail(
            r.title,
            r.description,
            'yourgmail@gmail.com',
            [r.email],
        )
        r.sent = True
        r.save()
