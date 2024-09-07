from django import forms
from django.forms import ModelForm
from .models import Invoice, InvoiceItem, Product

from django.forms import ModelForm


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'delivery_cost']

InvoiceItemFormSet = forms.inlineformset_factory(
    Invoice, InvoiceItem, fields=['product', 'quantity'], extra=1, can_delete=True
)



# from django.forms import ModelForm
# from .models import Task,Project

# from django.forms import DateInput

# class TaskForm(ModelForm):
#   class Meta:
#       model =Task
#       fields ='__all__'
#       widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
#                attrs={'type': 'date' }),
#                }

# class ProjectForm(ModelForm):
#   class Meta:
#       model =Project
#       fields ='__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Product Price'}),
            'description': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Product Description'}),
        }

