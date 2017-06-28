from django.db import models

class Product(models.Model):
	juid = models.IntegerField(primary_key=True)
	category = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	net_weight = models.IntegerField()
	brand = models.CharField(max_length=50)

class Books(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	isbn = models.IntegerField()
	author_firstname = models.CharField(max_length=50)
	author_middlename = models.CharField(max_length=50)
	author_lastname = models.CharField(max_length=50)

class Cosmetics(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_type = models.CharField(max_length=50)

class Electronics(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	subcategory = models.CharField(max_length=50)

class Food(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	subcategory = models.CharField(max_length=50)


