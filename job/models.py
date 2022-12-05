from django.db import models
 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

# def image_upload(instance, filename):
#     filename, extension = filename.split(".")
#     return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)
0
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
    image = models.ImageField(upload_to='media/jobs')
    # image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)

        super(Jobs,self).save(*args,**kwargs)
    def __str__(self) :
        return self.title

class Apllyjob(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=60)
    website = models.URLField()
    cv = models.FileField(upload_to='files/')
    cover_letter = models.TextField(max_length=255)

    def __str__(self):
        return self.name +' -- '+ self.job.title