# invoices/urls.py
from django.urls import path
from .views import create_invoice, invoice_list, generate_pdf, view_invoice

urlpatterns = [
    path('create/', create_invoice, name='create_invoice'),
    path('', invoice_list, name='invoice_list'),
    path('pdf/<int:invoice_id>/', generate_pdf, name='generate_pdf'),  # Pass invoice_id as a URL parameter
    path('view/<int:invoice_id>/', view_invoice, name='view_invoice'),
]
