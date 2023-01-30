from .models import Delivery
from django.forms import ModelForm


class DeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['Date', 'product', 'inventory', 'type', 'amount']

