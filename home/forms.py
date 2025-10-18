from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = ['p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date']

        widgets={
            'booking_date': forms.DateInput(attrs={'type':'date'}),
        }
         
        labels ={
            'p_name':'Patient Name',
            'p_phone':'Patient Phone',
            'p_email':'Patient Email',
            'doc_name':'Doctor',
            'booking_date':"Booking Date"
        }