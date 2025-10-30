from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','price','date','store','place']
        widgets={
            'date':forms.DateInput(attrs={'type':'date'}),
        }