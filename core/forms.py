from django import forms
from .models import Save

class SaveForm(forms.ModelForm):
    class Meta:
        model = Save
        fields = ['cotacao', 'ffo_yield', 'dividend_yield', 'p_vp', 'valor_mercado', 'liquidez', 'cap_rate', 'vacancia']
        widgets = {
            'cotacao': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'ffo_yield': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'dividend_yield': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'p_vp': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'valor_mercado': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'liquidez': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'cap_rate': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
            'vacancia': forms.TextInput(attrs={'type': 'range', 'min': '0', 'max': '100'}),
        }
