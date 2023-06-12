from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Product_category(models.Model):
    category_name = models.CharField(max_length=50)
    category_id = models.IntegerField()
    
    
    def __str__(self):
        return self.category_name
    
    
class  Product(models.Model):
    category_name = models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pid = models.IntegerField()
    pname = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    Date = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.pname
       

