from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = '__all__'
        widgets = {
            'remind_date': forms.DateInput(attrs={'type': 'date'}),
            'remind_time': forms.TimeInput(attrs={'type': 'time'}),
        }
