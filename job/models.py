from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Jobs(models.Model):
    fulltime = 'FT'
    parttime = 'PT'
    job_type_choices = [
        (fulltime,'Fulltime'),
        (parttime,'Parttime'),
    ]
    title = models.CharField(max_length=100)
    # Location
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=2,choices=job_type_choices,default=fulltime)
    description = models.TextField(max_length=500)
    pulished_at = models.DateTimeField(auto_now=True)
    vecancy = models.IntegerField(default = 1)
    salary = models.DecimalField(decimal_places=3,max_digits=8,default=1.1)
    experience = models.IntegerField(default=1)

    def __str__(self) :
        return self.title