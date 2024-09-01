from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # def save(self, *args, **kwargs):
    #     # Calculate total cost from related invoice items
    #     total_cost = sum(item.product.price * item.quantity for item in self.items.all())
    #     # Add delivery cost
    #     total_cost += self.delivery_cost
    #     self.total_cost = total_cost
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'Invoice #{self.id}' - {self.customer_name}

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
