from django.contrib import admin

# import models here 
from .models import Jobs,Category,Apllyjob

# Register your models here.
admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(Apllyjob)