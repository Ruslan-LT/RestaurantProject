from unittest.mock import patch

from django import forms
import re

class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.BooleanField(required=False)
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[
        ('Картою', 'Картою'),
        ('Картою/грошима при отриманні', 'Картою/грошима при отриманні')
    ])
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефону повинен містити у собі лише цифри")

        pattern = re.compile(r'^(380\d{9}|0\d{9})$')
        if not pattern.match(data):
            raise forms.ValidationError("Невірний формат номера телефону. Використовуйте 380XXXXXXXXX або 0XXXXXXXXX")
        return data
