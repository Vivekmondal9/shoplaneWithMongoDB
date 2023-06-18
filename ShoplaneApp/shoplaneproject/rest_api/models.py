from djongo import models

# Create your models here.
class UserSignup(models.Model):
    user_id=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    confirmPassword=models.CharField(max_length=200)


class Ratings(models.Model):
    # rating_id=models.AutoField(primary_key=True)
    id=models.IntegerField(primary_key=True)
    rate=models.FloatField()
    count=models.IntegerField()

    class Meta:
       abstract = False
    
class Products(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.TextField()
    price=models.FloatField()
    description=models.TextField()
    category=models.TextField()
    image=models.CharField(max_length=5000)
    rating=models.EmbeddedField(model_container=Ratings,null=True)
    # rating=Ratings(models.Model) #Creating an object of Ratings class
