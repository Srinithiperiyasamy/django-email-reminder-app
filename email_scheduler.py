from datetime import datetime
from django.core.mail import send_mail
from reminders.models import Reminder
import time

def start_email_scheduler():
    print("🚀 Scheduler STARTED")

    while True:
        now = datetime.now()
        print("⏰ Now:", now)

        reminders = Reminder.objects.filter(sent=False)

        for r in reminders:
            remind_dt = datetime.combine(r.remind_date, r.remind_time)
            print("🔍 Reminder at:", remind_dt)

            if now >= remind_dt:
                print("📧 Sending email to:", r.email)
                send_mail(
                    r.title,
                    r.description,
                    None,
                    [r.email],
                    fail_silently=False
                )
                r.sent = True
                r.save()

        time.sleep(30)
