from sre_constants import CATEGORY_DIGIT
from django.db import models

from django.contrib.auth.models import User

class Sign_up(models.Model):
    
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10,null=True)
    contact_no = models.CharField(max_length=10,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    regDate = models.DateField(max_length=10,null=True)
    updationDate = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    confirmed = models.BooleanField(default=False)

    def create_user(self):
        user = User.objects.create_user(
            username=self.email,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            
            last_name=self.last_name,
        )
        return user
    def __str__(self):
        return f"{self.first_name} {self.last_name}"







class events(models.Model):
    title = models.CharField(max_length=100, null=True)
    
    venue=models.CharField(max_length=20,null=True)
    dress=models.CharField(max_length=20,null=True)        
    Time = models.DateTimeField(null=True)
    Fee=models.IntegerField(null=True)
    confirmed_users = models.ManyToManyField(User, blank=True, related_name='confirmed_events')
    def _str_(self):
        return self.title 






class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    description = models.TextField()
    image=models.ImageField(null=True)

    def __str__(self):
        return self.name








class Register(models.Model):
    userreg = models.ForeignKey(Sign_up, on_delete=models.CASCADE)
    dance = models.ManyToManyField(Category)
    Age = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.userreg.first_name} {self.userreg.last_name}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
   

    def _str_(self):
        return self.title 
    

class user_login(models.Model):
    type=models.CharField(max_length=50,null=True,default="user")
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)


class confirmed_events(models.Model):
    user=models.ForeignKey(Sign_up,on_delete=models.CASCADE)
    event=models.ForeignKey(events,on_delete=models.CASCADE)
    ontime=models.DateTimeField(auto_now=True)

    def __str__(self):
        f= f"{self.user.first_name} booked {self.event.title}"
        return f