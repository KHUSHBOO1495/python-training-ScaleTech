from django.db import models

class Product(models.Model):
    """
    Represents a product.
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        """Return the product name when the object is displayed."""
        return self.name