from django.db import models

class User(models.Model):
    sellerID = models.CharField(max_length=300,unique=True)
    firstName = models.CharField(max_length=100,)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    profilePicURL = models.CharField(max_length=100,default="")
    def __str__(self) -> str:
        return self.firstName

class Orders(models.Model):
    orderID = models.CharField(max_length=300,unique=True)
    stockCode = models.CharField(max_length=100,)
    description = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()
    date = models.DateField()
    customerID = models.CharField(max_length=300)
    sellerID = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.customerID

class Products(models.Model):
    productID = models.CharField(max_length=300,unique=True)
    brand = models.CharField(max_length=100,)
    category = models.CharField(max_length=100)
    asin = models.CharField(max_length=100)
    modelNumber = models.IntegerField()
    sellerID = models.ForeignKey(User,on_delete=models.CASCADE)
    productURL = models.CharField(max_length=300)
    spec = models.CharField(max_length=300)
    technicalDetails = models.CharField(max_length=300)
    about = models.CharField(max_length=300)
    price = models.FloatField()
    def __str__(self) -> str:
        return self.id

class BundleProducts(models.Model):
    id = models.AutoField(primary_key=True)
    sellerID = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.id

class ProductBundles(models.Model):
    id = models.AutoField(primary_key=True)
    bundleProductID = models.ForeignKey(BundleProducts,on_delete=models.CASCADE)
    productID = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.id

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=300)
    textContent = models.CharField(max_length=300)
    reviewDate = models.DateField()
    productID = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.id

class Sentiment(models.Model):
    id = models.AutoField(primary_key=True)
    reviewID = models.ForeignKey(Reviews,on_delete=models.CASCADE)
    postiveRate = models.IntegerField()
    negativeRate = models.IntegerField()
    nuetralRate = models.IntegerField()
    overallSentiment = models.CharField(max_length=100,unique=True)
    def __str__(self) -> str:
        return self.id


