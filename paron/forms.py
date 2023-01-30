from .models import Delivery, Product, Inventory
from django.forms import ModelForm
from django import forms


class DeliveryForm(ModelForm):
    DELIVERY_TYPE_CHOICES = [
        ('Inleverans', 'Inleverans'),
        ('Utleverans', 'Utleverans')
    ]
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select)
    inventory = forms.ModelChoiceField(queryset=Inventory.objects.all(), widget=forms.Select)
    type = forms.ChoiceField(widget=forms.Select,
                             choices=DELIVERY_TYPE_CHOICES)

    class Meta:
        model = Delivery
        fields =  '__all__'
