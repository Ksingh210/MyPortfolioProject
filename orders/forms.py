from django import forms
from .models import Order

class Orderform(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('store',
                  'time',
                  'gardensoil',
                  'gardensoilpallets',
                  'pottingmix',
                  'pottingmixpallets',
                  'raisedbed',
                  'raisedbedpallets')
        widgets = {
            'gardensoilpallets':forms.TextInput(attrs={'size': '1'}),
            'pottingmixpallets': forms.TextInput(attrs={'size': '1'}),
            'raisedbedpallets': forms.TextInput(attrs={'size': '1'}),
        }