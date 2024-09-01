from django import forms
from .models import Invoice, InvoiceItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name', 'delivery_cost']

InvoiceItemFormSet = forms.inlineformset_factory(
    Invoice, InvoiceItem, fields=['product', 'quantity'], extra=1, can_delete=True
)



# invoices/forms.py
# from django import forms
# from .models import Invoice, InvoiceItem

# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ['customer_name', 'delivery_cost']  # Add all necessary fields

# class InvoiceItemForm(forms.ModelForm):
#     class Meta:
#         model = InvoiceItem
#         fields = ['product', 'quantity', 'line_total']
