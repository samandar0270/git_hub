from django.db import models

STATUS=[
    (1,'ACTIVE'),
    (2,'INACTIVE'),
    (3,'SOLD'),
    (3,'EXPIRED'),
]

class Registr(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField()
    passvord=models.CharField(max_length=10)


class Poster(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=25)
    adres=models.CharField(max_length=30)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    registr=models.ForeignKey(Registr, on_delete=models.CASCADE) #REGISTR
    sity=models.CharField(max_length=25)


class Category(models.Model):
    parent_id=models.IntegerField(default=None)
    icon=models.CharField(max_length=30)
    name=models.CharField(max_length=35)
    amount=models.IntegerField(default=None)


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    poster=models.ForeignKey(Poster,on_delete=models.CASCADE) #poster
    title=models.CharField(max_length=40)
    description=models.TextField(max_length=700)
    photo=models.ImageField(upload_to='images')
    price=models.IntegerField()
    create_at=models.DateTimeField()
    views=models.IntegerField(default=None)
    sale=models.IntegerField()
    status=models.CharField(max_length=20,choices=STATUS)

class PrisingPlan(models.Model):
    icon=models.CharField(max_length=30)
    prise=models.IntegerField()
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

