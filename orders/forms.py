from django import forms
from .models import Order

class Orderform(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('store','time', 'gardensoil', 'pottingmix', 'raisedbed')
        labels = {'store': 'Store', 'time':'Time', 'gardensoil':'Garden Soil', 'pottingmix':'Potting Mix', 'raisedbed':'Raised Bed'}