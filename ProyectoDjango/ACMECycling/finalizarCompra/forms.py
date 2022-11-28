from django import forms
from .models import Venta

class VentaCreateForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['nombre', 'email', 'dirreccion', 'metodoPago']