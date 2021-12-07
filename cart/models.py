from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Payment(models.Model):
    method = models.CharField(max_length=255,null=False,blank=False)
    is_active = models.BooleanField(default=True)
    des = models.TextField(default='')
class Order(models.Model):
    status_choice = (
        (0,'Đang chờ phê duyệt'),
        (1,'Chờ lấy hàng'),
        (2,'Đang giao'),
        (3,'Đã giao đến người dùng')
    )
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    tax = models.PositiveSmallIntegerField(default=0.1)
    status = models.PositiveSmallIntegerField(choices=status_choice,default=0)
    price_ship = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)],default=1.5)
    receiving_address = models.TextField(null=False,blank=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    total_price = models.FloatField(null=False,blank=False,validators=[MinValueValidator(0)])
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
class OrderItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=False, blank=False)
    order = models.ForeignKey(Order, models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)
    des = models.TextField(default='')

    def __str__(self):
        return self.product.name
class Cart(models.Model):
    status_choice = (
        (0, 'not working'),
        (1, 'working')
    )
    user = models.OneToOneField('user.User',on_delete=models.CASCADE,primary_key=True)
    status = models.PositiveSmallIntegerField(choices=status_choice, default=1)
    des = models.TextField(default='')

    def __str__(self):
        return self.user
class CartItem(models.Model):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,null=False,blank=False)
    cart = models.ForeignKey(Cart,models.CASCADE,null=False,blank=False)
    quantity = models.PositiveIntegerField(default=1)
    active = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False,default=0)
    des = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name
