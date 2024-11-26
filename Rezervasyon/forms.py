from django import forms
from .models import Rezervasyon

class RezervasyonForm(forms.ModelForm):
    reservation_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    
    class Meta:
        model = Rezervasyon
        fields = ['table_number', 'reservation_time', 'phone_number']