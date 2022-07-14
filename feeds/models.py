from django.db import models
from ckeditor.fields import RichTextField


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    # avatar = models.URLField(blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    # avatar=models.ImageField(upload_to='main_home')

    cv = models.FileField(upload_to='cv', blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    mycv = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class RecentWork(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='main_home')

    def __str__(self):
        return self.title

class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.skill
    
# class Contact(models.Model):
#     Name=models.CharField(max_length=80,blank=False,default="")
#     Email=models.EmailField(max_length=254,blank=False,default="")
#     Subjects=models.CharField(max_length=250 ,blank=False,default="")
#     Messages=models.TextField(max_length=2000,blank=False,default="")
class MyModel(models.Model):
    Full_Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=255, blank=False,default="")
    Subject = models.CharField(max_length=400,default="")
    Messages=models.TextField()
    search_fields = ["Full_Name"]
    
class Allwork(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    skill = models.TextField(max_length=330, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio')
    search_fields = ["title"]
    def __str__(self):
        return self.title
    