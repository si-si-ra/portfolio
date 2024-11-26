from django.db import models

# Create your models here.


class Portfolio(models.Model):
    image=models.ImageField(upload_to='images')
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class About(models.Model):
    description = models.TextField(max_length=5000)
    name = models.CharField(max_length=200)  # e.g., UI/UX Designer & Web Developer
    bio = models.TextField()  # Brief description or bio
    birthday = models.DateField()  # e.g., 1 May 1995
    email = models.EmailField()  # e.g., email@example.com
    phone = models.CharField(max_length=20)  # e.g., +123 456 7890
    address = models.CharField(max_length=200)  # e.g., New York, USA
    age = models.IntegerField()  # e.g., 30
    degree = models.CharField(max_length=100)  # e.g., Master
    github = models.URLField()  # e.g., www.example.com
    freelance = models.CharField(max_length=50)  # e.g., Available
    profile_image = models.ImageField(upload_to='profile_images/')  # Profile image upload


    def __str__(self):
        return self.name


 
class Skill(models.Model):
    skill = models.CharField(max_length=100)  
    proficiency = models.IntegerField()  # e.g., 55 for 55% proficiency

    def __str__(self):
        return self.skill

    

class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')  
    title = models.CharField(max_length=100, default="Resume")  
    def __str__(self):
        return self.title


class Summary(models.Model):
    name = models.CharField(max_length=100)  
    bio = models.TextField()  
    address = models.CharField(max_length=200) 
    phone = models.CharField(max_length=20)  
    email = models.EmailField() 
    def __str__(self):
        return self.name

    
class Education(models.Model):
    degree = models.CharField(max_length=200)  
    duration = models.CharField(max_length=100)  
    institution = models.CharField(max_length=200)  
    place = models.TextField(max_length=200)  
    description = models.TextField()  
    def __str__(self):
        return self.degree


class Experience(models.Model):
    position=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    place=models.TextField(max_length=200)
    def __str__(self):
        return self.position
    

class Project(models.Model):
    category_choices = [
        ('app', 'App'),
        ('web', 'Web'),
        ('design', 'Design'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=50, choices=category_choices)  # For filter like 'filter-app'
    details_link = models.URLField(max_length=500, blank=True)  # Link to details page or external link

    def __str__(self):
        return self.title


class Service(models.Model):
    ICON_CHOICES = [
        ('bi-briefcase', 'Briefcase'),
        ('bi-card-checklist', 'Checklist'),
        ('bi-bar-chart', 'Bar Chart'),
        ('bi-binoculars', 'Binoculars'),
        ('bi-brightness-high', 'Brightness High'),
        ('bi-calendar4-week', 'Calendar Week'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)  # Icon choices
    details_link = models.URLField(max_length=500, blank=True)  # Optional link to service details

    def __str__(self):
        return self.title



class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location=models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"Contact Info - {self.address}"
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

