#
from django.db import models
#
from ckeditor.fields import RichTextField
#######################################################################################################
# PERSONAL INFO MODEL


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
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    mycv = models.URLField(blank=True, null=True)
    my_pic = models.ImageField(upload_to='main_home')

    def __str__(self):
        return self.name_complete

#######################################################################################################
# ABOUT MODEL


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

#######################################################################################################
# RECENT WORK MODEL


class RecentWork(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='main_home')

    def __str__(self):
        return self.title

#######################################################################################################
# SKILL LANGUGES MODEL


class Skill_Language(models.Model):
    logos = models.ImageField(upload_to='main_home')
    logo_name = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.logo_name

#######################################################################################################
# CONTACT QUERY MODEL


class MyModel(models.Model):
    Full_Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=255, blank=False, default="")
    Subject = models.CharField(max_length=400, default="")
    Messages = models.TextField()

    def __str__(self):
        return self.Full_Name 

#######################################################################################################
# ALL WORK MODEL


class Allwork(models.Model):
    title = models.CharField(max_length=80, blank=True, null=True)
    skill = models.TextField(max_length=330, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio')
    search_fields = ["title"]

    def __str__(self):
        return self.title

#######################################################################################################
