from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(null=True)

class Cart(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE, null=False)
    create_date = models.DateTimeField(auto_now_add=True, null=False)
    expired_in = models.IntegerField(null=False, default=60)

class CartItem(models.Model):
    cart = models.ForeignKey("shop.Cart", on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey("shop.Product", on_delete=models.CASCADE, null=False)
    amount = models.IntegerField(null=False, default=1)

class Order(models.Model):
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE, null=False)
    order_date = models.DateField(auto_now_add=True, null=False)
    remark = models.TextField(null=True)

class OrderItem(models.Model):
    order = models.ForeignKey("shop.Order", on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey("shop.Product", on_delete=models.CASCADE, null=False)
    amount = models.IntegerField(null=False, default=1)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)

# class product_category(models.Model):
#     product_category_id = models.ForeignKey("shop.ProductCategory", unique=False, on_delete=models.CASCADE, primary_key=True)
#     product_id = models.ForeignKey("shop.Product", unique=False, on_delete=models.CASCADE, primary_key=True)

class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    categories = models.ManyToManyField("shop.ProductCategory")

class Payment(models.Model):
    order = models.OneToOneField("shop.Order", on_delete=models.CASCADE, null=False)
    payment_date = models.DateField(auto_now_add=True, null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentItem(models.Model):
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE, null=False)
    order_item = models.OneToOneField("shop.OrderItem", on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class PaymentMethod(models.Model):
    qr = "QR"
    credit = "CREDIT"
    payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE, null=False)
    method_choices = {qr : "QR CODE", credit : "CREDIT"}
    method = models.CharField(choices=method_choices, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    # def __str__(self):
    #     return self.method

    # myvenv\Scripts\activate.bat
    #foriegn key : ON DELELTE -> cascade, set_null, do_nothing, protect  