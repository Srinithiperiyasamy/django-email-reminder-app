from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm
from django.core.mail import send_mail
from django.http import HttpResponse


def test_email(request):
    send_mail(
        subject="Test Email",
        message="If you got this, email works",
        from_email="yourgmail@gmail.com",
        recipient_list=["YOUR_EMAIL@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email Sent")


def home(request):
    reminders = Reminder.objects.all().order_by('-remind_date', '-remind_time')
    return render(request, 'reminders/home.html', {'reminders': reminders})

def add_reminder(request):
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        reminder = form.save(commit=False)
        reminder.sent = False   # FORCE sent=False
        reminder.save()
        return redirect('/')
    return render(request, 'reminders/add.html', {'form': form})

def edit_reminder(request, id):
    reminder = get_object_or_404(Reminder, id=id)
    form = ReminderForm(request.POST or None, instance=reminder)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'reminders/add.html', {'form': form})


def delete_reminder(request, id):
    reminder = get_object_or_404(Reminder, id=id)
    reminder.delete()
    return redirect('home')
