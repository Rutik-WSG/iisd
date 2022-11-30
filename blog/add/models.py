from django.db import models

# Create your models here.
class Userlogin(models.Model):
    username  = models.CharField(max_length=12)
    password    = models.CharField(max_length=50,unique=True)
    email       = models.EmailField(max_length=20)

    def __str__(self):
        return self. username
    
    
class blog(models.Model):
    id=models.IntegerField(primary_key=True)
    header=models.CharField(max_length=12)
    img=models.ImageField()
    short_description=models.CharField(max_length=50)
    Aartical=models.CharField(max_length=1000)
    #tags = models.ManyToManyField(User, related_name='tasks')
    
    def __str__(self):
        return self.header
    
class BookMark(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    user = models.ForeignKey(blog, on_delete=models.CASCADE, related_name="user_bookmark")
    address = models.CharField(max_length=150)
    # latitude = models.DecimalField(max_digits=20, decimal_places=12)
    # longitude = models.DecimalField(max_digits=20, decimal_places=12)

    def __str__(self):
        return self.address
    
class Comment(models.Model):
   
    id=models.IntegerField(primary_key=True)
    header =  models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_total_likes(self):
        return self.likes.users.count()

    def get_total_dis_likes(self):
        return self.dis_likes.users.count()

    def __str__(self):
        return str(self.comment)[:30]
    
    

class CategoryType(models.Model):
    CHOICES = (
        ('coding', 'coding'),
        ('playing', 'playing'),
        ('danceing', 'danceing'),
        ('singing', 'singing'),)
    id = models.IntegerField(primary_key=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50,blank=False,choices=CHOICES)        