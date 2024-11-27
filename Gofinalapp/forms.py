from django import forms
from Gofinalapp.models import Contact, Appointment ,ImageModel


class ContactForm(forms.ModelForm):
    class Meta:
        model =Contact
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model =Appointment
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'
