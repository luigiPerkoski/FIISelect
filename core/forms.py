from django import forms
from .models import Save
from .controller import Result

Result.result()

mi = Result.min_result
ma = Result.max_result


class SaveForm(forms.ModelForm):
    class Meta:
        model = Save
        fields = ['cotacao', 'ffo_yield', 'dividend_yield', 'p_vp', 'valor_mercado', 'liquidez', 'cap_rate', 'vacancia']
        widgets = {
            'cotacao': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["cotacao"]}', 'max': f'{ma["cotacao"]}'}),
            'ffo_yield': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["ffo_yield"]}', 'max': f'{ma["ffo_yield"]}'}),
            'dividend_yield': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["dividend_yield"]}', 'max': f'{ma["dividend_yield"]}'}),
            'p_vp': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["p_vp"]}', 'max': f'{ma["p_vp"]}'}),
            'valor_mercado': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["valor_mercado"]}', 'max': f'{ma["valor_mercado"]}'}),
            'liquidez': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["liquidez"]}', 'max': f'{ma["liquidez"]}'}),
            'cap_rate': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["cap_rate"]}', 'max': f'{ma["cap_rate"]}'}),
            'vacancia': forms.TextInput(attrs={'type': 'range', 'min': F'{mi["vacancia"]}', 'max': f'{ma["vacancia"]}'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(required=False, max_length=100, label=False)
