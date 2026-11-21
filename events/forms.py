
from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = [
            'name',
            'description',
            'date',
            'time',
            'location',
            'price',
            'image_file'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter event name'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your event',
                'rows': 4
            }),
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter event location'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter ticket price',
                'min': '0'
            }),
            'image_file': forms.ClearableFileInput(attrs={
                'accept': 'image/*'
            })
        }
