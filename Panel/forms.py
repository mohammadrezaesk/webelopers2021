from django import forms
from Panel.models import Product


class EditForm(forms.Form):
    class Meta:
        model = Product
        fields = ('name', 'price', 'quantity', 'tag', 'image')
        widgets = {
            "name": forms.TextInput(attrs={'name': "name", "class": "form-control"}),
            "price": forms.TextInput(attrs={'name': "price", "class": "form-control"}),
            "quantity": forms.TextInput(attrs={'name': "quantity", "class": "form-control"}),
            "tag": forms.TextInput(attrs={'name': "tag", "class": "form-control"}),
            # "image": forms.FileField(attrs={'id': "product_image", 'name': "image"})
        }
