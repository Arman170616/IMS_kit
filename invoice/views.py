from django.shortcuts import render, redirect
from .models import Invoice
from .forms import InvoiceForm, InvoiceItemFormSet
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.forms import formset_factory



# invoices/views.py
from django.shortcuts import render, redirect
from django.forms import formset_factory
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm


def create_invoice(request):
    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        if invoice_form.is_valid() and formset.is_valid():
            invoice = invoice_form.save()
            items = formset.save(commit=False)
            for item in items:
                item.invoice = invoice
                item.line_total = item.product.price * item.quantity
                item.save()
            # Update total cost
            invoice.total_cost = sum(item.line_total for item in invoice.items.all()) + invoice.delivery_cost
            invoice.save()
            # Generate PDF (placeholder)
            return redirect('invoice_list')
    else:
        invoice_form = InvoiceForm()
        formset = InvoiceItemFormSet()
    return render(request, 'create_invoice.html', {'invoice_form': invoice_form, 'formset': formset})




# def create_invoice(request):
#     InvoiceItemFormSet = formset_factory(InvoiceItemForm, extra=1)  # Create a formset from InvoiceItemForm

#     if request.method == 'POST':
#         invoice_form = InvoiceForm(request.POST)
#         formset = InvoiceItemFormSet(request.POST)

#         if invoice_form.is_valid() and formset.is_valid():
#             # Create the invoice
#             invoice = invoice_form.save(commit=False)
            
#             # Initialize total cost
#             total_cost = 0

#             # Save the formset data
#             invoice.save()  # Save invoice first to get the invoice ID

#             for form in formset:
#                 if form.cleaned_data:  # Check that form has data
#                     item = form.save(commit=False)
#                     item.invoice = invoice  # Link item to the created invoice
#                     item.save()

#                     # Calculate total cost for the invoice
#                     total_cost += item.product.price * item.quantity
            
#             # Add the delivery cost to total cost
#             invoice.total_cost = total_cost + invoice.delivery_cost
#             invoice.save()  # Save the updated total cost

#             return redirect('invoice_list')
#         else:
#             # Print form errors for debugging
#             print("Invoice Form Errors:", invoice_form.errors)
#             print("Formset Errors:", formset.errors)
#     else:
#         invoice_form = InvoiceForm()
#         formset = InvoiceItemFormSet()

#     return render(request, 'create_invoice.html', {'invoice_form': invoice_form, 'formset': formset})



def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_list.html', {'invoices': invoices})


# invoices/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Invoice
from weasyprint import HTML
from django.template.loader import render_to_string


def generate_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    html_content = render_to_string('invoice_pdf.html', {'invoice': invoice})
    pdf_file = HTML(string=html_content).write_pdf()
    
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
    return response


def view_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice_detail.html', {'invoice': invoice})