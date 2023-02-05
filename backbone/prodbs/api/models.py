from django.db import models

class User(models.Model):
    id = models.CharField(max_length=300,primary_key=True)
    firstName = models.CharField(max_length=100,)
    lastName = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    profilePicURL = models.CharField(max_length=100,default="")
    def __str__(self) -> str:
        return self.firstName+" "+self.id

class Orders(models.Model):
    id = models.CharField(max_length=300,primary_key=True)
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
    id = models.CharField(max_length=300,primary_key=True)
    brand = models.CharField(max_length=100,)
    category = models.CharField(max_length=100)
    asin = models.CharField(max_length=100)
    modelNumber = models.IntegerField()
    sellerID = models.ForeignKey(User,on_delete=models.CASCADE)
    productURL = models.CharField(max_length=300)
    spec = models.TextField()
    technicalDetails = models.TextField(max_length=300)
    about = models.CharField(max_length=300)
    price = models.FloatField()
    def __str__(self) -> str:
        return str(self.id)

class BundleProducts(models.Model):
    id = models.AutoField(primary_key=True)
    sellerID = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id)

class ProductBundles(models.Model):
    id = models.AutoField(primary_key=True)
    bundleProductID = models.ForeignKey(BundleProducts,on_delete=models.CASCADE)
    productID = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id)

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=300)
    textContent = models.TextField()
    reviewDate = models.DateField()
    productID = models.ForeignKey(Products,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.id)

class Sentiment(models.Model):
    id = models.AutoField(primary_key=True)
    reviewID = models.ForeignKey(Reviews,on_delete=models.CASCADE)
    positiveRate = models.FloatField()
    negativeRate = models.FloatField()
    neutralRate = models.FloatField()
    overallSentiment = models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.id)




