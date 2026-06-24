from django import forms
from datetime import date
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['is_expired']
    

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'p_name': 'Patient Name',
            'p_email': 'Patient Email',
            'p_phone': 'Patient Phone',
            'booking_date': 'Booking Date',
            'doc_name': 'Doctor Name',
        }
  