'''m django import forms

class LoginForm(forms.Form):
    rollno = forms.CharField(max_length=15, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


from django import forms

class LoginForm(forms.Form):
    rollno = forms.CharField(max_length=15, required=True)
    password = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=True
    )

'''
from django import forms
from .models import *
class UploadExcelForm(forms.Form):
    file = forms.FileField()


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['notification', 'due_date', 'end_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class NotificationDropdownForm(forms.Form):
    notification = forms.ModelChoiceField(
        queryset=Notifications.objects.all().order_by('-start_date'),
        empty_label="Select a Notification",
        label="Notification",
    )
