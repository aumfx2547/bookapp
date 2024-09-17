from django.db import models
    
class product_data(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, null=True)
    product_qty = models.IntegerField(null=True)
    product_price = models.IntegerField(null=True)
    product_detail =models.TextField(null=True)

    product_image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    def __str__(self):
        return self.product_name

class order_data(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_total = models.IntegerField(null=True)
    order_date = models.DateField(null=True)
    order_address = models.CharField(max_length=200,null=True)
    order_tel = models.CharField(max_length=11,null=True)
    order_username = models.CharField(max_length=100,null=True)
    order_email = models.EmailField(max_length=100,null=True)
    
    def __str__(self):
        return self.order_id

class order_detail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    order_id_ref = models.ForeignKey(order_data,null=True,on_delete=models.CASCADE)
    prod_id = models.ForeignKey(product_data,null=True,on_delete=models.CASCADE)
    prod_qty = models.IntegerField(null=True)
    prod_price = models.IntegerField(null=True)
    def __str__(self):
        return self.detail_id

class cart_add(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product_data,null=True,on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=True)
    product_price = models.IntegerField(null=True)
    email = models.EmailField(max_length=100,null=True)

    def __str__(self):
        return self.email
