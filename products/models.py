from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models

# Create your models here.
from commons.models import BaseItem, BaseImage
class ImageProduct(BaseImage):
    products = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True, related_name='image_product',blank=True)
class Color(models.Model):
    color = models.CharField(max_length=30,null=False, default='white')
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    def __str__(self):
        return self.color

class Category(BaseItem):
    def __str__(self):
        return self.name

class Brand(BaseItem):
    image = models.CharField(max_length=255,
                             default='https://i-ione.vnecdn.net/2020/10/24/news-content-156134682977-2706-1603489782.jpg')
    country = models.CharField(max_length=255,default='Viet Nam')

    def __str__(self):
        return self.name
class Tag(BaseItem):
    def __str__(self):
        return self.name

class Product(BaseItem):
    price = models.DecimalField(max_digits=10,decimal_places=2,null=False,validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=1000)
    amount_sold = models.PositiveIntegerField(default=0)
    hot = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class InfoProductBook(models.Model):
    author = models.CharField(max_length=255,null= True, blank=True)
    headline = models.CharField(max_length=255,null= True, blank=True)
    pub_date = models.DateField(blank=True,null=True)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(0)])
    number_of_pages = models.PositiveIntegerField(null=True, blank=True)
    product = models.OneToOneField(Product,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return self.product.name

class InfoProductElectric(models.Model):
    choice_memory =  (
        (4, '4MB'),
        (8, '8MB'),
        (16,'16MB'),
        (32,'32MB'),
        (64, '64MB')
    )
    choice_storage = (
        (32, '32G'),
        (64, '64G'),
        (128, '128G'),
        (256, '256G'),
        (512, '512G'),
        (1024, '1TB'),
    )
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    display_technology = models.CharField(max_length=50,default=None)
    screen_resolution = models.CharField(max_length=50,default=None)
    chip = models.CharField(max_length=50,null=True,blank=True)
    camera = models.CharField(max_length=20,default=None)
    memory = models.IntegerField(choices=choice_memory,null=True,blank=True)
    storage = models.IntegerField(choices=choice_storage,null=True,blank=True)
    battery_capacity = models.IntegerField()

    def __str__(self):
        return self.product.name

class ProductView(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s" % (self.product.name, self.views)
class BaseAction(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=False)
    creator = models.ForeignKey('user.User',on_delete=models.CASCADE)

    class Meta :
        abstract = True
class ProductComment(BaseAction):
    content = models.TextField(default=None)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.product.name
class RecommentProduct(BaseAction):
    product_comment = models.ForeignKey(ProductComment,on_delete=models.CASCADE)

class Action(BaseAction):
    like,haha,angry = range(0,3)
    actions = [
        (like,'like'),
        (haha,'haha'),
        (angry,'angry')
    ]
    type = models.PositiveSmallIntegerField(choices=actions,default=like)

    def __str__(self):
        return self.product.name

class Rating(BaseAction):
    rate = models.PositiveSmallIntegerField(default=0,validators=[MaxValueValidator(5)])
    def __str__(self):
        return self.product.name